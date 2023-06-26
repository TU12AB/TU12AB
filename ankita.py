num1=float(input("enter the no 1:"))
num2=float(input("enter the no 2:"))
operator=input("enter the operator:")
if operator=='+':
    print(num1+num2)
elif operator=='-':
        print(num1-num2)
elif operator=='*':
    print(num1*num2)
    if operator=='/':
    print(num1/num2)
else:
    print("invalid operator")
