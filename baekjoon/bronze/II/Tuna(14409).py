n, x, *A = map(int, open(t := 0).read().split())
while A:
    a, b, *A = A
    if abs(a - b) > x:
        a, *A = A
        t += a
    else:
        t += max(a, b)
print(t)
