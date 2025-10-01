a  = int(input("Enter a number a:"))
b = int(input("Enter a number b:"))
c = int(input("Enter a number c:"))


ans = (b*b)-(4*a*c)
if ans<0:
    print("less than 0")
elif ans>0:
    print("greater than 0")
else:
    print("equal to 0")

