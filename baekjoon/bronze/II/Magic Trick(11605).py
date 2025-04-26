_, *A = open(s := 0).read().split()
O = [*zip(A[::2], map(int, A[1::2]))]
for i in range(100):
    i += 1
    for o, n in O:
        if 'A' == o[0]:
            i += n
        if 'S' == o[0]:
            i -= n
        if 'M' == o[0]:
            i *= n
        if 'D' == o[0]:
            i /= n
        if i % 1 or i < 0:
            s += 1
            break
print(s)
