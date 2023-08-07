T = []
for i in range(int(input())):
    c, b, n, r = map(int, input().split())
    *A, = map(int, input().split())
    t = 0
    for _ in ' '*n:
        a, b = map(int, input().split())
        t += (a in A)*r*b//100
    T += f"Data Set {i+1}:\n{t}",
print('\n\n'.join(T))
