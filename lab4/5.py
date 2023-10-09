N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    color = int(input())
    a.add(color)
for _ in range(M):
    color = int(input())
    b.add(color)
f = a.intersection(b)
s = a.difference(b)
t = b.difference(a)
print(len(f))
print(*sorted(f))

print(len(s))
print(*sorted(s))

print(len(t))
print(*sorted(t))