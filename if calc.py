operator = input("enter an operator (+ - * / %): ")

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "":
    print("please enter a valid operator")
elif operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
elif operator == "%":
    result = num1 % num2
    print(round(result, 3))
else:
    print("please enter a valid operator")
