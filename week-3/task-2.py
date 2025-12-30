print("=== Task 2.1 - Hexagon Area using Triangle ===")

def triangle_area(base, height):
    return 0.5 * base * height

a = float(input("Enter hexagon side length a: "))

triangle_height = 0.866 * a
one_triangle = triangle_area(a, triangle_height)
hexagon_area = 6 * one_triangle

print("Each triangle area:", one_triangle)
print("Hexagon area (6 triangles):", hexagon_area)
print()

print("=== Task 2.2 - Three Rectangles Areas ===")

print("Rectangle 1:")
side1_r1 = float(input("Side 1: "))
side2_r1 = float(input("Side 2: "))
area1 = side1_r1 * side2_r1
print("Area:", area1)
print()

print("Rectangle 2:")
side1_r2 = float(input("Side 1: "))
side2_r2 = float(input("Side 2: "))
area2 = side1_r2 * side2_r2
print("Area:", area2)
print()

print("Rectangle 3:")
side1_r3 = float(input("Side 1: "))
side2_r3 = float(input("Side 2: "))
area3 = side1_r3 * side2_r3
print("Area:", area3)

print("\nAll done!")
