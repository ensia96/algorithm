k, w, m = map(int, input().split())
x, y = divmod(w-k, m)
print(x+bool(y))
