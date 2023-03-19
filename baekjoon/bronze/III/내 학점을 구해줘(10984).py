for _ in ' '*int(input()):
    A = B = 0
    n = int(input())
    for _ in ' '*n:
        a, b = map(float, input().split())
        A += a
        B += a*b
    print(int(A), f'{B/A:.1f}')
