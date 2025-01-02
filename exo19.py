unique_words = set()
while True:
    word=input("Enter a word : ")
    if word in unique_words:
        break
    unique_words.add(word)

print(f"You typed in {len(unique_words)} unique words.")