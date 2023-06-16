for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(f'Case #{i+1}:', 'YNEOS'[a*a+b*b != c*c::2])
