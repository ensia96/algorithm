a, b, c, n = map(int, input().split())
print(+any(a*i+b*j+c*k == n for i in range(n//a+1)
      for j in range(n//b+1)for k in range(n//c+1)))
