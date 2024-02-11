a, b, c, d, e, f, g, h, i = map(int, open(0).read().split())
T = [0]*101
for i in [*range(d, e)]+[*range(f, g)]+[*range(h, i)]:
    T[i] += 1
print(T.count(1)*a+T.count(2)*b*2+T.count(3)*c*3)
