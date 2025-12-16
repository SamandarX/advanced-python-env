word = input("Enter a word: ")
n = int(input("Enter a number: "))

for ch in word:
    for i in range(n):
        print(ch, end="")
    print()
