for _ in ' '*int(input()):
    a, b = map(int, input().split())
    A = [*map(sum, zip(*[[*map(int, input().split())]for _ in ' '*b]))]
    print(A.index(max(A))+1)
