n, f, r = int(input()), input(), range
a, m = n//2, -2**32
for c in r(2**a):
    b = [*map(int, bin(c)[2:].zfill(a))]
    if any(b[i]*b[i-1]for i in r(1, a)):
        continue
    i, t = 0, []
    while i < n:
        i, t = (i+3, t+[str(eval(f[i:i+3]))])\
            if i+2 < n and b[i//2]*(not i % 2)else(i+1, t+[f[i]])
    for i in r(1, len(t), 2):
        t[i+1] = str(eval(''.join(t[i-1:i+2])))
    m = max(m, int(t.pop()))
print(m)
