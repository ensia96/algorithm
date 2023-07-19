for i in range(int(input())):
    a, b, c, d, e = map(int, input().split())
    print(f'Case {i+1}:',
          'YNEOS'[(abs(d-b), abs(e-c))not in [(1, 2), (2, 1)]::2])
