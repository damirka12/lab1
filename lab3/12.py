


numbers = [int(s) for s in input().split()]
k, c = [int(k) for k in input().split()]
numbers.append(0)

for i in reversed(range(k, len(numbers))):
    numbers[i] = numbers[i - 1]
numbers[k] = c

for val in numbers:
    print(val)



