n = int(input())

for i in range(1, n+1):
    num_str = str(i)
    divisible = True
    for digit in num_str:
        d = int(digit)
        if d == 0 or i % d != 0:
            divisible = False
            break
    if divisible:
        print(i, end=" ")

print()

m = int(input())
A = list(map(int, input().split()))

def swap_first_last(arr):
    if len(arr) >= 2:
        arr[0], arr[-1] = arr[-1], arr[0]

print("Original:", *A)
swap_first_last(A)
print("Result:", *A)
