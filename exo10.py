word = input("Type a word: ")
palindrome = True

l=len(word) // 2
for i in range(l):
    if word[i] != word[-(i + 1)]:
        palindrome = False
        break

if palindrome:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")