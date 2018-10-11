print("Input a word to reverse: ")
word = input()

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")

#alternate method

print("Please enter a word")
userWord = str(input())
print(userWord[::-1])
