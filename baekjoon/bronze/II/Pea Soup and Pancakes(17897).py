I = input
R = []
n = int(I())
for _ in ' ' * n:
    k = int(I())
    r = I()
    M = [I()for _ in ' ' * k]
    if any(m == 'pancakes'for m in M) * any(m == 'pea soup'for m in M):
        R += r,
print((R + ['Anywhere is fine I guess'])[0])
