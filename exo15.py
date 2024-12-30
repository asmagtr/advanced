string = input("Please type in a string: ")
vowels= ['a', 'e', 'o']
for vowel in vowels:
    if vowel in string:
        print(vowel+" found")
    else:
        print(vowel+" not found")