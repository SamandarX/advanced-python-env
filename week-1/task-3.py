A = float(input())

integer_part = int(A)
fractional_part = int((A - integer_part) * 100)

new_number = fractional_part + integer_part / 100

print(new_number)
