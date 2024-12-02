a, b, c, d = map(int, open(0).read().split())
T = [a + ~-a // 8 * d, c + b + ~-b // 8 * (2 * c + d)]
print("ZDiopk"[T.index(min(T)) :: 2])
print(min(T))
