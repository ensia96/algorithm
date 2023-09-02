k, a, x, b, y = map(int, open(0).read().split())
print(max((k-a)*x+(k-a-b)*y, (k-a-b)*x+(k-b)*y))
