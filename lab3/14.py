

numbers = [int(s) for s in input().split()]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == numbers[j] and i != j:
            break
    else:
        print(numbers[i])



