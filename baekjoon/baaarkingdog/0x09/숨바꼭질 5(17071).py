n, k = map(int, input().split())
m = int(5 * 10e4)
l = [0] * (m + 1)
q, r = [(n, 0)], -1

for p, t in q:
    x = k + (t*(1+t)//2)
    if p == x:
        exit(print(t))
    if x > m:
        break
    for a in [p-1, p+1, p*2]:
        if 0 < a <= m:
            q += [(a, t+1)]

print(r)
