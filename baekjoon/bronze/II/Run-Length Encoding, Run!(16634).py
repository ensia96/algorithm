t, M = input().split()
if 'D' < t:
    l, c = M[0], 0
    for m in M[1:]:
        if l[-1] != m:
            l += str(c)+m
            c = 0
        c += 1
    print(l+str(c))
else:
    print(''.join(a*int(b)for a, b in zip(M[::2], M[1::2])))
