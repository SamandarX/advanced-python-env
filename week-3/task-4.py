def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

numer = A * D
denom = B * C
g = gcd(numer, denom)
print(numer//g, denom//g)

xa, ya, R2 = map(int, input().split())
def inside_circle(x, y):
    return (x-xa)**2 + (y-ya)**2 <= R2

p1, p2 = map(int, input().split())
f1, f2 = map(int, input().split())
l1, l2 = map(int, input().split())

count = 0
if inside_circle(p1, p2): count += 1
if inside_circle(f1, f2): count += 1
if inside_circle(l1, l2): count += 1
print(count)
