


n, k = [int(s) for s in input().split()]
result = ['I'] * n

for i in range(k):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        result[j] = '.'

for i in range(n):
    print(result[i], end='')

