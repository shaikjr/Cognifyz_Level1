#Task4: Calculator Program

#Create a Python program that acts as a basic
#calculator. It should prompt the user to
#enter two numbers and an operator (+
#, -,
#*
#, /,
#%), and then display the result of the
#operation.

user1 = float(input("enter first number:"))
user2 = float(input("enter second number:"))
operator = input("enter a operator(+,-,*,/,//): ")

if operator == "+":
    result = user1+user2
elif operator == "-":
    result = user1-user2
elif operator == "*":
    result = user1-user2
elif operator == "%":
    result = user1%user2
elif operator == "/":
    result =user1/user2
elif operator == "//":
    result=user1//user2

else:
    print("Invalid operator")
    result = None

if result is not None:
    print("Result:", result)