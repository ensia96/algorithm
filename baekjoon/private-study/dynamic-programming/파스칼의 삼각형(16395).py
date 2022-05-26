n, k, f = *map(int, input().split()), lambda x: x < 2 or x*f(x-1)
print(f(n-1)//(f(n-k)*f(k-1)))
