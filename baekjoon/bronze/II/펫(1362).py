f, i = lambda: input().split(), 1
o = w = 0
while 1:
    a, b = f()
    if a == '0':
        break
    if a == '#':
        print(i, [':-'+'()'[o/2 < w < 2*o], 'RIP'][w < 0])
        i += 1
    elif a in 'EF':
        w += int(b)*(1-2*(a == 'E'))*(w > 0)
    else:
        o, w = map(int, [a, b])
