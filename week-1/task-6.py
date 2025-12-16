a = float(input("First number: "))

op = input("Operation (+, -, *, /): ")

b = float(input("Second number: "))

if op == "+":
    result = a + b
    print(a, "+", b, "=", result)

elif op == "-":
    result = a - b
    print(a, "-", b, "=", result)

elif op == "*":
    result = a * b
    print(a, "*", b, "=", result)

elif op == "/":
    if b != 0:
        result = a / b
        print(a, "/", b, "=", result)
    else:
        print("Error: division by zero")

else:
    print("Invalid operation")
