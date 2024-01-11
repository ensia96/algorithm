n, *A, b, c = map(int, open(0).read().split())
x = 0
for a in A:
    a -= b
    x += 1+(-(a//-c)if a > 0 else 0)
print(x)
