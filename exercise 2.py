# Exercise 2 shopping cart program

item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"your total is: {total}")