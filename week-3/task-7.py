def right_triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(length, width):
    return length * width

X, Y, Z, T = map(int, input().split())

area1 = right_triangle_area(X, Y)
area2 = right_triangle_area(Z, T)
total_area = area1 + area2

print(total_area)

n = int(input())
octal = oct(n)[2:]
padded = octal.zfill(10)
print(padded)
