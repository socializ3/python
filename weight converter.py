#weight converter

weight = float(input("enter the weight of a person: "))
unit = input("kilograms or pounds? (kg or lb): ")

if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"the weight of said person is {round(weight, 3)} {unit}")
elif unit == "lb":
    weight = weight / 2.205
    unit = "kgs"
    print(f"the weight of said person is {round(weight, 3)} {unit}")
else:
    print(f"{unit} is invalid")


