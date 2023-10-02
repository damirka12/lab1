


numbers = [int(s) for s in input().split()]
counter = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            counter += 1

print(counter)

