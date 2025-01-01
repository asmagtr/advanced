numbers = [1, 2, 3, 4, 5]

# we define a function to enter a value since we're going to use more than once
def get_value():
    while True:
        try:
            user_choice=int(input("enter a value: "))
            return user_choice
        except ValueError:
            print("Invalid input type, must enter a number")

#same thing for index
def get_index(list):
    l=len(list)
    while True:
        try:
            user_choice=int(input("enter the index: "))
            if 0<=user_choice< l:
                break
            else:
                print("out of index range")
        except ValueError:
            print("Invalid input type, must enter a number")

    return user_choice

while True:
    print("menu:")
    print("1. append")
    print("2. insert")
    print("3. pop")
    print("4. remove")
    print("5. quit")

    while True:
        try:
            user_choice=int(input("pick an option : "))
            if 1<= user_choice <= 5 :
                break
            else:
                print("the number must be between 1 and 5")
        except ValueError:
            print("Invalid input type, must enter a number")

    match user_choice:
        case 1:
            new=get_value()
            numbers.append(new)
            print(f"new list {numbers}")
        case 2:
            new_val=get_value()
            new_index=get_index(numbers)
            numbers[new_index]=new_val
            print(f"new list {numbers}")
        case 3:
            numbers.pop()
            print(f"new list {numbers}")
        case 4:
            value=get_value()
            if value in numbers:
                numbers.remove(value)
                print(f"new list {numbers}")
            else:
                print(f"there is no iccurence of the number {value} in numbers list")
        case 5:
            break

print("thanks for playin!")




   