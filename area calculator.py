length = float(input("enter the length of the rectangle: "))
width = float(input("enter the width of the rectangle: "))
height = float(input("enter the height of the rectangle: "))

#because were dealing with math, the float variable has to be used within the input
#you can find the area with this by removing height ofc
#by adding both the area and volume variable with the correct equations you can solve both of the equations


volume = length * width * height
area = length * width

print(f"the area of the rectangle is {volume} cm^3")
print(f"the area of the rectangle is {area} cm^2")

