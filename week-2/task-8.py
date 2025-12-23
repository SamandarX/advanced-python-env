s1 = input().strip()
s2 = input().strip()

if len(s1) != len(s2):
    print("NO")
else:
    sorted_s1 = ''.join(sorted(s1))
    sorted_s2 = ''.join(sorted(s2))
    
    if sorted_s1 == sorted_s2:
        print("YES")
    else:
        print("NO")
