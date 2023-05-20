h, w = map(int, input().split())
print(min(max(h/2, w/3), max(h/3, w/2)))
