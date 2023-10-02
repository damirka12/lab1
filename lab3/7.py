


numbers = [int(s) for s in input().split()]
l = int(input())
a = 1

for i in range(0, len(numbers)):
    if numbers[i] >= l:
        a += 1

print(a)



