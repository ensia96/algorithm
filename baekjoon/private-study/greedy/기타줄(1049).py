n, m = map(int, input().split())
x = y = 6000
for _ in ' '*m:
    a, b = map(int, input().split())
    x, y = min(x, a), min(y, b)
print(n*y if x > 6*y else min(x*(n//6+1), x*(n//6)+y*(n % 6)))
