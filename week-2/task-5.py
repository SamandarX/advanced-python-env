letters = "ABCEHKMOPTXY"

n = int(input())

for i in range(n):
    code = input().strip()

    if len(code) != 6:
        print("No")
        continue
    
    check = True
    
    if code[0] not in letters:
        check = False
    
    for j in range(1, 4):
        if not code[j].isdigit():
            check = False

    if code[4] not in letters or code[5] not in letters:
        check = False
    
    if check:
        print("Yes")
    else:
        print("No")
