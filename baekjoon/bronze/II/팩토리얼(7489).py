n, *A = map(int, open(0))
for a in A:
    for i in range(1, a):
        a *= i
    print(str(a).rstrip("0")[-1])
