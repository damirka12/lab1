

def isVis (a):
    kr4 = a%4
    kr100 = a%100
    kr400 = a%400
    if(kr4 == 0):
        if(kr100 != 0): print("YES")
        else:
            if(kr400 == 0): print("YES")
            else: print("NO")
    else: print("NO")

    # if (kr4 == 0 & kr400 != 0 & kr100 != 0): print("YES")
    # else: print("NO")


a = int(input())
isVis(a)

