#if statements mean that a line of code will run only IF said condition is true
#     else just means it with do something else lol

age = int(input("enter your age: "))

if age >=100:
    print("damn old ahh go drink some tea")
elif age >= 18:
    print("you are old enough! sign up now.")
elif age < 0:
    print("you haven't even been born yet")
else:
    print("you must be old enough to do it!")

