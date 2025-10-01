number = int(input("Enter a Number: "))

factorial = 1
while number >= 0:
    if number == 0:
        factorial *= 1
    else:
        factorial *= number

    number -= 1

print(factorial)