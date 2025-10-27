# import important libraries
import cv2
import face_recognition
import os
from datetime import datetime


#define the FaceRecognitionSystem class
class FaceRecognitionSystem:
    def __init__(self, path_to_students):
        self.path_to_students = path_to_students #this is the folder path which have classes not a section
        self.encode_dict_known = {} #to encode a face of student
        self.marked_attendance = set() #if attandace was marked
        self.load_known_faces() #load the students face for encoding

    def load_known_faces(self):
        for classes in os.listdir(self.path_to_students):
            for section in os.listdir(os.path.join(self.path_to_students, classes)):
                for file in os.listdir(os.path.join(self.path_to_students, classes ,section)):
                    if file.endswith(".jpg"):
                       image_path = os.path.join(self.path_to_students,classes, section ,file)
                       img = cv2.imread(image_path)
                       name = os.path.splitext(file)[0]  # Extract name from file name
                       encode = self.find_encodings(img)
                       if encode is not None:  # Check if a face encoding is found
                           self.encode_dict_known[name] = (classes, section, encode)


    def find_encodings(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img)
        face_encodings = face_recognition.face_encodings(img, face_locations)
        if len(face_encodings) == 1:  # Ensure only one face is detected
            return face_encodings[0]
        else:
            return None
        
    def mark_attendance(self, name, class_name,section):
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        class_attendance_file = os.path.join('attendance', class_name, section, f'{date_string}.csv')
        os.makedirs(os.path.dirname(class_attendance_file), exist_ok=True) # Create directory if not exists
        
        with open(class_attendance_file, 'a+') as f:
            if (self.check_attendance(name,class_name,section,f)):
                    dtString = now.strftime('%H:%M:%S')
                    f.write(f'{name},{dtString}\n')
                    
            else:
                pass

    def check_attendance(self,name, class_name,section,f):
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        class_attendance_file = os.path.join('attendance', class_name,section, f'{date_string}.csv')
        with open(class_attendance_file,'r') as f:
            students_present = f.readlines()
            present = []
            for student in students_present:
                student_details = student.split(',')
                present.append(student_details)
            if present == []:
                return True
            else:
                for student_detail in present:
                    if student_detail[0] == name:
                        return False
                    else:
                        return True


    def recognize_faces(self, frame):
        # Find all the faces and their encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Compare faces found in the current frame with known faces
        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            name = "Unknown"
            class_name = ""
            section = ""

            for known_name, (known_class,known_section ,known_encode) in self.encode_dict_known.items():
                match = face_recognition.compare_faces([known_encode], face_encoding, tolerance=0.5)
                if match[0]:
                    name = known_name
                    class_name = known_class
                    section = known_section
                    break

            # Draw rectangle around the face and write the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Mark attendance if not already marked
            if name != "Unknown" and (name, class_name, section) not in self.marked_attendance:
                self.mark_attendance(name, class_name,section)
                self.marked_attendance.add((name, class_name,section))

    def start_recognition(self):
        # Load webcam
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            # Recognize faces in the current frame
            self.recognize_faces(frame)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release handle to the webcam
        cap.release()
        cv2.destroyAllWindows()

        # Clear marked attendance after recognition cycle
        self.marked_attendance.clear()


# Example usage
if __name__ == "__main__":
    FaceRecognitionSystem('students').start_recognition()