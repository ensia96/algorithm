l, *L = open(0)
a, b, c = map(int, l.split())
for l in L:
    n = int(l)
    if n < b:
        print(f'NTV: Dollar dropped by {b-n} Oshloobs')
    if c < n:
        print(f'BBTV: Dollar reached {n} Oshloobs, A record!')
        c = n
    b = n
