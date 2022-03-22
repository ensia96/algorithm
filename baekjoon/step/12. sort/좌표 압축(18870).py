n = int(input())
a, c, d = [*map(int, input().split())], 0, {}
for i in sorted(set(a)):
    d[i] = c
    c += 1
print(*map(lambda x: d[x], a))
