

numbers = input().split()
for i in range(1, len(numbers)):
    numbers[i] = int(numbers[i])
    if numbers[i] > int(numbers[i - 1]):
        print(numbers[i], end=' ')





