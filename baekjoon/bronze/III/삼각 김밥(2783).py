x, y = map(int, input().split())
print(min(eval(input().replace(*' /'))*1000 for _ in ' '*int(input())))
