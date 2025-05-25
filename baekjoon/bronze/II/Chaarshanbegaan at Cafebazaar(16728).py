_, *A = map(int, open(0).read().split())
print(int(sum(10-abs(-(((x*x+y*y)**.5-10)//-20))
      for x, y in zip(A[::2], A[1::2]))))
