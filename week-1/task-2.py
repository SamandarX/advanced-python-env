a, b, c = map(int, input().split())

max_salary = a
min_salary = a

if b > max_salary:
    max_salary = b
if c > max_salary:
    max_salary = c

if b < min_salary:
    min_salary = b
if c < min_salary:
    min_salary = c

print(max_salary - min_salary)
