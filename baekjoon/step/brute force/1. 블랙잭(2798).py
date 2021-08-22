n, m = map(int, input().split())
l = list(map(int, input().split()))
x = 0

for a in l:
    for b in l:
        for c in l:
            if a == b or a == c or b == c:
                continue
            d = a + b + c
            if d <= m:
                x = max(x, d)

print(x)
