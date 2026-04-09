# logical operators means a conditional statment

#     and = checks two or more conditions if they are True
#     or = checks if at LEAST one condition is True
#     not = True if condition is False, and vice versa

unit = input("is the temperature in celsius or fahrenheit? (C / F): ")
temp = float(input("enter the temperature: "))

if unit == "C":
    temp = round((temp * 9)/5 + 32, 2)
    unit = "F"
    print(f"the temperature is {temp} {unit}")
elif unit == "F":
    temp = round((temp -32) * 5/9, 2)
    unit = "C"
    print(f"the temperature is {temp} {unit}")
else:
    print(f"the {unit} is invalid")



