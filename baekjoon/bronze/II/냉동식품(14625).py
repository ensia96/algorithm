a, b, c, d, e = map(int, open(0).read().split())
print(sum(str(e) in f"{i//60:02}:{i%60:02}" for i in range(a * 60 + b, c * 60 + d + 1)))
