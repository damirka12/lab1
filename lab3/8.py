


numbers = input().split()
a = 1

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        a += 1

print(a)

