import sys
i = sys.stdin.readline
l, _ = lambda: [*map(int, i().split())], 0

for _ in range(int(i())):
    _, a, b = i(), l(), l()
    print(sum(i > j for i in a for j in b))
