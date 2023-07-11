for i in ' '*int(input()):
    print(*[round(sum(i)/10)
          for i in zip(*[[*map(int, input().split())]for _ in ' '*10])])
