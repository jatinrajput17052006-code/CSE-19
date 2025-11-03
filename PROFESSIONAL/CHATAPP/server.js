const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

const PORT = process.env.PORT || 3000;
const HISTORY_FILE = 'chat_history.json';

let chatHistory = loadChatHistory();
let activeUsers = {};

function loadChatHistory() {
  try {
    const data = fs.readFileSync(HISTORY_FILE, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    console.log('Error loading chat history:', error.message);
    return [];
  }
}

function saveChatHistory() {
  try {
    fs.writeFileSync(HISTORY_FILE, JSON.stringify(chatHistory, null, 2), 'utf8');
  } catch (error) {
    console.log('Error saving chat history:', error.message);
  }
}

io.on('connection', (socket) => {
  console.log('A user connected');

  // Listen for login event
  socket.on('login', (username) => {
    activeUsers[socket.id] = username;
    io.emit('userList', Object.values(activeUsers));
    io.emit('userSeparator', username);
  });

  // Send chat history to the newly connected client
  const socketUsername = activeUsers[socket.id];
  const userChatHistory = chatHistory.filter(entry => entry.username === socketUsername);
  socket.emit('chatHistory', userChatHistory);

  // Listen for new messages
  socket.on('message', (data) => {
    const { username, message } = data;
    chatHistory.push({ username, message });
    io.emit('message', { username, message });
    saveChatHistory();
  });

  // Disconnect event
  socket.on('disconnect', () => {
    const username = activeUsers[socket.id];
    delete activeUsers[socket.id];
    io.emit('userList', Object.values(activeUsers));
    console.log(`${username} disconnected`);

    // Remove messages of the disconnected user from the UI
    // io.emit('removeUserMessages', username);
  });
});

app.use(express.static('public'));

server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
