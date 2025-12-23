n, m = map(int, input().split())
a = input()
words = set()

for i in range(n - m + 1):
    word = a[i:i + m]
    words.add(word)

print(len(words))
