n, k, *L = map(int, open(0).read().split())
print(len({c.index(m)
      for i in range(k)if (c := L[i::k]).count(m := max(c)) < 2}))
