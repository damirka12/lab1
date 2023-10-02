


numbers = input().split()
numbers = [int(x) for x in numbers]
for i in range(0, len(numbers), 2):
    print(numbers[i], end=' ')


