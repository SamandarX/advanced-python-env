a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print(a, "+", b, "=", a + b)

elif op == "-":
    print(a, "-", b, "=", a - b)

elif op == "*":
    print(a, "*", b, "=", a * b)

elif op == "/" and b != 0:
    print(a, "/", b, "=", a / b)

elif op == "/" and b == 0:
    print("Error: division by zero")

else:
    print("Invalid operation")
