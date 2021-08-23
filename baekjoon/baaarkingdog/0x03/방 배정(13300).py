n, k = map(int, input().split())
l = [[0, 0] for _ in range(6)]

for _ in range(n):
    s, y = map(int, input().split())
    l[y - 1][s] += 1

print(sum([x // k + bool(x % k) + y // k + bool(y % k) for x, y in l]))
