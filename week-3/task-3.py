def hypotenuse(a, b):
    return (a*a + b*b)**0.5

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

hyp1 = hypotenuse(a1, b1)
hyp2 = hypotenuse(a2, b2)

print(hyp1)
print(hyp2)

if hyp1 > hyp2:
    print("First hypotenuse bigger")
elif hyp2 > hyp1:
    print("Second hypotenuse bigger")
else:
    print("Equal")

s = input()
words = s.split()
new_words = []
for word in words:
    letters = list(word)
    letters.sort()
    new_word = ""
    for let in letters:
        new_word = new_word + let
    new_words.append(new_word)

result = " ".join(new_words)
print(result)
