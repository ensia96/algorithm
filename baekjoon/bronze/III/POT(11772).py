A = 0
for l in [*open(0)][1:]:
    x, y = divmod(int(l), 10)
    A += x**y
print(A)
