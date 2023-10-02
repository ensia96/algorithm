n, r, s = map(int, input().split())
for _ in ' '*n:
    t = [r-i for i in range(r)if '#' in input()]
    print(max(t)-min(t))
