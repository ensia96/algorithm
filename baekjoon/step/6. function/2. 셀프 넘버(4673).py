a = [0] + [1] * 10000
for i in range(1, 10001):
    i += sum(map(int, str(i)))
    if i <= 10000:
        a[i] = 0
for i, j in enumerate(a):
    if j:
        print(i)
