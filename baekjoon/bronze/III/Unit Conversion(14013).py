x, y = map(float, input().split())
for _ in ' '*int(input()):
    n, N = input().split()
    n = float(n)
    print(n/x*y if N == 'A'else n/y*x)
