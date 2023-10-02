



numbers = [int(s) for s in input().split()]
k = int(input())

if k >= 0 and k < len(numbers):
    numbers = numbers[:k] + numbers[k+1:]

for val in numbers:
    print(val)



