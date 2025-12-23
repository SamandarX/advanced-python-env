a = input()
count = 0

for i in range(len(a)):
    if a[i:i+5] == ">>-->":
        count += 1
    if a[i:i+5] == "<--<<":
        count += 1
print(count)
