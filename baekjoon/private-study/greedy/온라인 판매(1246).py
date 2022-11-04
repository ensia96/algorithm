n, m = map(int, input().split())
p = a = 0
for i, j in enumerate(sorted(int(input())for _ in ' '*m)):
    x = j*min(m-i, n)
    if x > p:
        a, p = j, x
print(a, p)
