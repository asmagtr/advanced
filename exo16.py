numbers = [1, 2, 3, 4, 5]
while True:
  index = int(input("Enter an index: "))
  if index == -1:
    break
  if 0 <= index < len(numbers):
    value = int(input("Enter a new value: "))
    numbers[index] = value
    print("Updated list:", numbers)
  else:
    print("Invalid index.")
