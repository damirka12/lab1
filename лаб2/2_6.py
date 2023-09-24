

a = int(input())
b = int(input())
c = int(input())

if(a==b==c): print("3")
else:
    if(a == b): print("2")
    elif(b==c): print("2")
    elif(a==c): print("2")
    else: print("0")
