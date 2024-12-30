amount = int(input("Total amount: "))
items = int(input("Number of items: "))
day = input("Day of the week: ")

if day in ["Saturday", "Sunday"]:
    discount = 0.20
else:
    discount = 0.10

if items > 5:
    discount += 0.05

price = amount * (1 - discount)
print(f"Total price after discount: {price} dinars")