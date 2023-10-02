


numbers = [int(x) for x in input().split()]
a = 0

for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        a += 1

print(a)