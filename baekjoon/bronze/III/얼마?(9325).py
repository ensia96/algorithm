for _ in ' '*int(input()):
    s = int(input())
    for _ in ' '*int(input()):
        q, p = map(int, input().split())
        s += q*p
    print(s)
