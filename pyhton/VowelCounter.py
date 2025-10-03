string =  str(input("Enter a string: "))

count = 0
for i in string:
    if i in "aeiouAEIOU":
        count+=1

if count!=0:
    print("Given string contain "+str(count)+" Vowels!")
else:
    print("Given string contain 0 Vowels!")
