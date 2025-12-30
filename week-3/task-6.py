def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())
g = gcd(a, b)
lcm = a * b // g
print(g, lcm)

a, b, c, d = map(int, input().split())
e1 = (a*a + b*b + c*c + d*d)/2
e2 = a*a + b*b - c*c
e3 = c*c + d*d - a*a
area1 = (e1 - e2)**0.5 * (e1 - e3)**0.5
print(area1)
