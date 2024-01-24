n, m = map(int, open(0))
print(min(i for i in range(100)if not (n//100*100+i) % m))
