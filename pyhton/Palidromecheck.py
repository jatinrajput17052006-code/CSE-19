string = str(input("Enter a string: "))

new_string = string[::-1]
if new_string ==  string:
    print(string+" is a Palindrome String!")
else:
    print(string+" is not a Palindrome String!")
