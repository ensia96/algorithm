x, l, r = map(int, input().split())
print(r if abs(x-l) > abs(x-r) else l)
