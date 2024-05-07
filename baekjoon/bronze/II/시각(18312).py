n, k = map(int, input().split())
M = 60
H = M*M
print(sum(k in divmod(i//H, 10)+divmod(i % H//M, 10)+divmod(i % M, 10)
      for i in range(-~n*M*M)))
