unit = input("is the temperature in celsius or fahrenheit? (C / F): ")
temp = float(input("enter the temperature: "))

if unit == "C":
    temp = round((temp * 9)/5 + 32, 2)
    unit = "F"
    print(f"the temperature is {temp} {unit}")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 2)
    unit = "C"
    print(f"the temperature is {temp} {unit}")

# now check if temperature is "good"
if unit == "C":
    if 21 <= temp <= 26:
        print("the temperature is good")
    else:
        print("the temperature is bad")

elif unit == "F":
    if 70 <= temp <= 80:
        print("the temperature is good")
    else:
        print("the temperature is bad")