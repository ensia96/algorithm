for _ in ' '*int(input()):
    n, x, y = map(int, input().split())
    a, *A, b = map(int, input().split())
    print('OEHBKAAOASRTYYDH'[(a == x)+2*(b == y)::4])
