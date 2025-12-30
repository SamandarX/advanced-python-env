def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

numer = A * D - B * C
denom = B * D

if numer < 0:
    numer = -numer
    denom = -denom

g = gcd(numer, denom)
print(numer//g, denom//g)

n = int(input())
divisors = []
for i in range(1, n+1):
    if n % i == 0:
        divisors.append(str(i))
print(" ".join(divisors))
