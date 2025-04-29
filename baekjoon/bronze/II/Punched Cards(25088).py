_, *A = map(int, open(t := 0).read().split())
for x, y in zip(A[::2], A[1::2]):
    f, t = lambda a, b: b.join(['', *a*y, '']), t+1
    print(f"Case #{t}:")
    x = [*f(*'-+').join(['']+['\n'+f(*'.|')+'\n']*x+[''])]
    x[0] = x[1] = x[2*y+2] = x[2*y+3] = '.'
    print(*x, sep='')
