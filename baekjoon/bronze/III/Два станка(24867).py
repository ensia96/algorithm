k, a, x, b, y = map(int, open(0).read().split())
t = max(0, k-a-b)
print(max(max(0, k-a)*x+t*y, t*x+max(0, k-b)*y))
