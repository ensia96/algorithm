_, a, b, *A = map(int, open(0).read().split())
print(a, b, *min((((x-a)**2+(y-b)**2)**.5, y, x)
      for x, y in zip(A[::2], A[1::2]))[::-1])
