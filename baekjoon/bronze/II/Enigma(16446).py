a, b = open(0)
print(sum(all(map(str.__ne__, a[i:], b[:-1]))
      for i in range(len(a) - len(b) + 1)))
