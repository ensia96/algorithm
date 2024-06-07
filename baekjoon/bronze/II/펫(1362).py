f, i = lambda: input().split(), 1
o = w = 0
while (A := f()) != [*'00']:
    a, b = A
    if a == '#':
        print(i, ['RIP', ':-'+'()'[o/2 < w < 2*o]][w > 0])
        i += 1
    elif a in 'EF':
        w += int(b)*(1-2*(a == 'E'))*(w > 0)
    else:
        o, w = map(int, A)
