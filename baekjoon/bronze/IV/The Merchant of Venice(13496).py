x, y = lambda: map(int, input().split()), int(input())
for i in range(y):
    n, s, d = x()
    S = 0
    i and print()
    for _ in ' '*n:
        a, b = x()
        S += (a <= s*d)*b
    print(f'Data Set {i+1}:\n{S}')
