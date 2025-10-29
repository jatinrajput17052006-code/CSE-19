#include <iostream>
#include <string>
using namespace std;    
bool isPalindrome(const string &str) {
    int left = 0;
    int right = str.length() - 1;
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}   
int main() {
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    if (isPalindrome(input)) {
        cout << "\"" << input << "\" is a palindrome." << endl;
    } else {
        cout << "\"" << input << "\" is not a palindrome." << endl;
    }
    return 0;
}   
    