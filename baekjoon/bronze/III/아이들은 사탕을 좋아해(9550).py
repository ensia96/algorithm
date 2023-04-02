for _ in ' '*int(input()):
    n, k = map(int, input().split())
    print(sum(a//k for a in map(int, input().split())))
