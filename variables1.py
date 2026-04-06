#variables are a reusable container for storing a value, like a number
#              a variable behaves as if it were the value it contains
# ex:

age = 17
print(age) #this will just print the variable unlike doing print("age") which would give the word "age"

#lets say you want to print the variable with a line of text like "i am __ years old"
#you need to add a string into the print as so

print("i am " + str(age) + " years old")
#as shown above, you can run this and it will print "i am 17 years old"
#make to sure consider your spacing, and adding the quotations before and after the string

#another way to do so is:
print("i am", age, "years old")
#just remember with this method, the spacing within the (, variable ,) counts as spacing in the print
#meaning you dont have to compensate for spacing

#one more way to do so is:
print(f"i am {age} years old")
#this methiod is fairly easy, but i just dont like how far apart my fingers have to come across the keyboard lol
