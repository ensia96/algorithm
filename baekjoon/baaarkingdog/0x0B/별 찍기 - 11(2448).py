def r(n, p=3, q=['*', '* *', '*****']):
    if n == 3:
        for i in range(p):
            q[p-i-1] = (' ' * i) + q[p-i-1]
        return q
    d = [*reversed(q)]
    for i in range(len(q)):
        d[i] = q[i] + d[i].replace('*', ' ') + q[i]
    q += d
    return r(n//2, p*2, q)


print('\n'.join(r(int(input()))))
