for _ in ' '*int(input()):
    e, n = map(int, input().split())
    print(sum(e < int(input())for _ in ' '*n))
