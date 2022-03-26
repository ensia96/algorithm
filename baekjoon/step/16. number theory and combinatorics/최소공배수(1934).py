for _ in ' '*int(input()):
    a, b = map(int, input().split())
    A = a*b
    while b:
        a, b = b, a % b
    print(A//a)
