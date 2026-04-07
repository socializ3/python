import math

#calculate the circum of a circle

math.pi
radius = float(input("what is the radius of the circle? ")) #added float because radius can be a decimal and input for user to type in radius


circumference = 2 * math.pi * radius

print(f"the circumference of the circle is {round(circumference, 2)}")



