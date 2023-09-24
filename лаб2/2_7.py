
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a == c:
    if b != d: print("YES")
    else: print("NO")
elif b == d:
    if a != c: print("YES")
    else: print("NO")
else: print("NO")