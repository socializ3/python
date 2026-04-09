unit = input("is the temperature in celsius or fahrenheit? (C / F): ")
temp = float(input("enter the temperature: "))

# check BEFORE converting
if unit == "C":
    if 21 <= temp <= 26:
        print("the temperature is good for swimming")
    else:
        print("the temperature is bad for swimming")

    converted = round((temp * 9)/5 + 32, 2)
    print(f"the temperature in fahrenheit is {converted} F")

elif unit == "F":
    if 70 <= temp <= 80:
        print("the temperature is good for swimming")
    else:
        print("the temperature is bad for swimming")

    converted = round((temp - 32) * 5/9, 2)
    print(f"the temperature in celsius is {converted} C")