f = lambda a, b: b * (a == 0) or f(b % a, a)
print(f(*map(int, input().split())))
