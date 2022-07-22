n, m = map(int, input().split())
A = sorted(zip([*map(int, input().split())], range(1, n+1)))
for _ in ' '*m:
    i, j, k = map(int, input().split())
    c = 0
    for x, y in A:
        c += i <= y <= j
        if c == k:
            print(x)
            break
