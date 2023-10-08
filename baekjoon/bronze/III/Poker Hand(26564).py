for _ in ' '*int(input()):
    A = [i[:1]for i in input().split()]
    print(max(map(A.count, A)))
