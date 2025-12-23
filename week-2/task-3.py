equation = input()
character = list(equation)
x_pos = character.index('x')
op = character[1]
result = int(character[4])

if x_pos == 0:
    num = int(character[2])
    if op == '+':
        x = result - num
    else:
        x = result + num
elif x_pos == 2:
    num = int(character[0])
    if op == '+':
        x = result - num
    else:
        x = num - result
else:
    num = int(character[0])
    if op == '+':
        x = num + result
    else:
        x = num - result

print(x)
