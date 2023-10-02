

numbers = [int(s) for s in input().split()]
min_val = min(numbers)
max_val = max(numbers)

min_index = numbers.index(min_val)
max_index = numbers.index(max_val)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

for val in numbers:
    print(val)


