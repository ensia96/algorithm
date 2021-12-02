t = 0
while 1:
    l, p, v, t, a = *map(int, input().split()), t+1, 0
    if not l:
        exit()
    print(f"Case {t}: {min(l,v%p)+(v//p*l)}")
