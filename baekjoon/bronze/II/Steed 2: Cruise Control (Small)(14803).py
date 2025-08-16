for i in range(int(input())):
    d, n = map(int, input().split())
    A = 1e18
    for _ in ' '*n:
        k, s = map(int, input().split())
        A = min(A, d/(d-k)*s)
    print(f'Case #{i+1}:', A)
