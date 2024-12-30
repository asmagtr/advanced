name = input("Please enter your name: ")

if name == "VIP":
    print("Enjoy the show for free!")
else:
    price = 15.50
    tickets = int(input("How many tickets would you like to buy? "))
    total = tickets *price
    print(f"The total cost is {total}")
    print("Enjoy your tickets!")