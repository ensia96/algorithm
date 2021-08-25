n = int(input())
t, a = [*map(int, input().split())], [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
    h = t[i]
    for j in range(i - 1, -1, -1):
        if h < t[j]:
            a[i] = j + 1
            break

print(*map(str, a))
