import math

#find the length of the hypotenuse of a right triangle
a = float(input("what is the length of side a? "))
b = float(input("what is the length of side b? "))

hypotenuse = math.sqrt(a ** 2 + b ** 2)


print(f"the length of the hypotenuse is {round(hypotenuse, 2)}")
