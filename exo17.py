numbers=[]
shoe_sizes=[]

for i in range(5):
    numbers.append(i+1)

for size in [8, 9, 10, 11, 12]:
    shoe_sizes.append(size)


print("numbers list:", numbers," shoe sizes list:", shoe_sizes)

#adding dublicates
numbers.append(3)
numbers.append(5)

##printing with the duplicates:
print("numbers list(with duplicates):", numbers)


combined_list = numbers + shoe_sizes
print("combined list:", combined_list)