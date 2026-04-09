# print ( welcome to simple calculator)

num1 = int(input("enter first number:"))
num2 = int(input("enter second number : "))

op = input("enter operataror :(+,-,*,/) ")

if op == "+":
    print (num1 + num2)
elif op=="-":
    print (num1-num2)
elif op == "*":
    print (num1 *num2 )
elif op =="/":
    print (num1/num2)
else:
    print ("invalid operator")