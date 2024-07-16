a, b, c = map(int, open(0).read().split())
for i in range(10):
    print(str(a * b * c).count(str(i)))
