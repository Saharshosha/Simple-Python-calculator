n1 = int(input("Enter a first number:"))
n2 = int(input("Enter a second number:"))
operation = input("Enter a operation (+, _, *, /) :")

if operation == "+":
    print (n1+n2)
elif operation == "-":
    print (n1-n2)
elif operation == "*":
    print (n1*n2)
elif operation == "/":
    print (n1/n2)
elif operation == "/":
    if n2 != 0:
        print (n1/n2)
    else:
        print ("Error : You can't divide by zero!")

else :
    print ("Please enter a valid operation")
    