for l in [*open(0)][:-1]:
    a, b = map(int, l.split())
    print(*max((sum(not i % j for j in range(1, i+1)), i)
          for i in range(a, b+1))[::-1])
