ticket = input("Enter a 6-digit ticket number: ")

first_three = ticket[:3]
last_three = ticket[3:]

sum_first = int(first_three[0]) + int(first_three[1]) + int(first_three[2])
sum_last = int(last_three[0]) + int(last_three[1]) + int(last_three[2])

if sum_first == sum_last:
    print("YES")
else:
    print("NO")
