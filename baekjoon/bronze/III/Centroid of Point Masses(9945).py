i, j = int(input()), 1
while i > 0:
    X = Y = M = 0
    for _ in ' '*i:
        x, y, m = map(int, input().split())
        X += x*m
        Y += y*m
        M += m
    print(f'Case {j}: {X/M:.2f} {Y/M:.2f}')
    input()
    j += 1
    i = int(input())
