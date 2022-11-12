n, l, k = map(int, input().split())
x = y = 0
for _ in ' '*n:
    a, b = map(int, input().split())
    if a <= l:
        x += a <= l
        y += b <= l
t = min(y, k)
print(140*t+100*(min(k-t, x-y)))
