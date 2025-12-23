items = input().split()

count = {}

for item in items:
    if item in count:
        count[item] = count[item] + 1
    else:
        count[item] = 1

print("Purchase frequency:")
for item in count:
    print(item + ":", count[item])

max_count = 0
popular = ""

for item in count:
    if count[item] > max_count:
        max_count = count[item]
        popular = item

print("Most popular item:", popular)

print("Purchased once:", end=" ")
for item in count:
    if count[item] == 1:
        print(item, end=" ")
print()

print("Sorted by frequency:")

products = list(count.keys())

for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if count[products[j]] > count[products[i]]:
            products[i], products[j] = products[j], products[i]

for p in products:
    print(p, count[p])
