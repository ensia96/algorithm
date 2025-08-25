while (C := input()) != '#':
    M, S = map(int, input().split())
    for _ in ' '*int(input()):
        t, a = input().split()
        a = int(a)
        S = [min(M, S+a), max(0, S-a)][t == 'S']
    print(C, S)
