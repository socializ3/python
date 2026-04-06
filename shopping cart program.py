item = input("what item would you like to purchase? ")
price = float(input("what is the price of said item? ")) #price can be decimals so we added a float
quantity = int(input("how many items would you like? ")) #quantity for at this store can only be bought within wholes so we add integer variable

total = price * quantity

print(f"you have bough {quantity} x {item}/s")
#print(f"your total is: ${total}.")

#with just this line of code you can find the price of the item by entering the name and price
#you can also round up to a whole number total liek this

print(f"your total is: ${round(total, 1)}")

#by running the code and inputing the same values you would get 49. bla bla bla
#with this the number after the "," is the decimal place you'd like to round to

