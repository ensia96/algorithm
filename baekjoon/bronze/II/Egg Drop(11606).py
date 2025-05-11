n, k = map(int, input().split())
x = 1
for _ in ' '*n:
    f, s = input().split()
    f = int(f)
    if 'A' in s:
        x = max(x, f)
    else:
        k = min(k, f)
print(x+1, k-1)
