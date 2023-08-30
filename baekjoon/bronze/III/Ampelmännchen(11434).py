T = []
for i in range(int(input())):
    n, w, e = map(int, input().split())
    t = 0
    for _ in ' '*n:
        a, b, c, d = map(int, input().split())
        t += max(a*w+c*e, e*d+b*w)
    T += f'Data Set {i+1}:\n{t}',
print('\n\n'.join(T))
