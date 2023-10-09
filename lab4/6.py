n = int(input())
list = []

for i in range(n):
    s = input().split()
    list.append(s)

a=set()
for i in range (len(list)):
    a.update(list[i])

print(len(a))