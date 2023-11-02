a, b, c = map(int, input().split())
print(+any(a == i*b+j*c for i in range(1, 150)for j in range(1, 150)))
