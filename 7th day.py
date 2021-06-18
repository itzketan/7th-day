"""
1.	Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value

Subtraction of two numbers is +value

Division of two numbers is +value

Multiplication of two numbers is +value

"""
def add(a, b) :
    return a + b
def sub(a, b) :
    return a - b
def mul(a, b) :
    return a * b
def div(a, b) :
    return a / b
print("Enter Two Integer Numbers : ")
nOne = int(input())
nTwo = int(input())
print("\n""Enter the Operator (+,-,*,/):")
ch = input()
if ch == '+':
    print("\n" "Addition of two numbers is : " + str(nOne) + " + " + str(nTwo) + " = " + str(add(nOne, nTwo)))
elif ch == '-':
    print("\n" "Subtraction of two numbers is : " + str(nOne) + " - " + str(nTwo) + " = " + str(sub(nOne, nTwo)))
elif ch == '*':
    print("\n" "Multiplication of two numbers is : " + str(nOne) + " * " + str(nTwo) + " = " + str(mul(nOne, nTwo)))
elif ch == '/':
    print("\n" "Division of two numbers is : " + str(nOne) + " / " + str(nTwo)+ " = " + str(div(nOne, nTwo)))
else:
    print("\nInvalid Operator!")
print("\n -------------------------------------------- 2 -------------------------------------------------------------")
"""
Create a function covid( ) & it should accept patient name, and body temperature, 
by default the body temperature should be 98 degree
"""
def covid(n,t):
    return (n,t)
def d(T = 98):
    return d(T = 98)
n = str(input("Enter Patient Name : "))
t = str(input("Enter Patient Body Temperature In Degree : "))

print("Patient Name : " + n)
if t != 98 :
    print("Patient Body Temperature : " + t + " Degree")
else:
    print("Default Temperature : " + d(T = 98) + " Degree")
