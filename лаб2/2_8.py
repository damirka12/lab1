

a = int(input())
b = int(input())
c = int(input())
d = int(input())


if(a==c):
    if( pow((b-d), 2) == 1): print("YES")
    else: print("NO")
elif(b==d):
    if (pow((a - c), 2) == 1):
        print("YES")
    else:
        print("NO")
else:
    if(pow((a - c), 2) == 1 & pow((b-d), 2)) == 1: print("YES")
    else: print("NO")