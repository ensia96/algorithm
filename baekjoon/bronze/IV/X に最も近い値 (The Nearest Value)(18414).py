x, l, r = map(int, input().split())
print(x if l <= x <= r else r if abs(x-l) > abs(x-r)else l)
