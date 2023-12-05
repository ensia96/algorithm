n, f = int(input()), lambda x: x < 1 or x*f(x-1)
print(f(n)//(f(5)*f(n-5)))
