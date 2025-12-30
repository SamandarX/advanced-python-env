print("=== Area Calculator ===")
print("1. Rectangle")
print("2. Triangle") 
print("3. Circle")
print("4. Square")
print("5. Quit")

while True:
    choice = int(input("Pick shape (1-5): "))
    
    if choice == 1:
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = length * width
        print("Rectangle area:", area)
        print()
        
    elif choice == 2:
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = 0.5 * base * height
        print("Triangle area:", area)
        print()
        
    elif choice == 3:
        radius = float(input("Radius: "))
        area = 3.14 * radius * radius
        print("Circle area:", area)
        print()
        
    elif choice == 4:
        side = float(input("Side: "))
        area = side * side
        print("Square area:", area)
        print()
        
    elif choice == 5:
        print("Bye!")
        break
        
    else:
        print("Wrong choice! Try 1-5")
        print()

print("\n=== Task 2 - Array sums and averages ===")

arr1 = [1, 2, 3, 4, 5]
sum1 = 0
for num in arr1:
    sum1 = sum1 + num
avg1 = sum1 / len(arr1)
print("Array 1:", arr1)
print("Sum:", sum1, "Average:", avg1)
print()
 
arr2 = [10, 20, 30]
sum2 = 0
for num in arr2:
    sum2 = sum2 + num
avg2 = sum2 / len(arr2)
print("Array 2:", arr2)
print("Sum:", sum2, "Average:", avg2)
print()

arr3 = [7, 14, 21, 28]
sum3 = 0
for num in arr3:
    sum3 = sum3 + num
avg3 = sum3 / len(arr3)
print("Array 3:", arr3)
print("Sum:", sum3, "Average:", avg3)
