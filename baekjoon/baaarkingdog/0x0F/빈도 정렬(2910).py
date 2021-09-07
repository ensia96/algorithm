i = input
_, l = i(), i().split()
print(*sorted(l, key=lambda x: (-l.count(x), l.index(x))))
