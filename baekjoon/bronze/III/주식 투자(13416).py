for _ in ' '*int(input()):
    print(sum(max(*map(int, input().split()), 0)for _ in ' '*int(input())))
