n, *A = open(0)
x = sum(min(100, int(l.replace(*"09").replace(*"69"))) for l in A) / int(n)
print(int(x // 1 + (x % 1 >= 0.5)))
