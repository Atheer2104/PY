word = input("Type a word to check if it's a palindrome: ")

a = []
for x in word:
    a.append(x)

b = a[::-1]
if a == b:
   print("The word is palindrome")
else:
    print("sorry the word is not palindrome")