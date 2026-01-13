N, X = map(int, input().split())
A = list(map(int, input().split()))

total = []

for i in A:
    if i < X:
        total.append(i)

print(*total)