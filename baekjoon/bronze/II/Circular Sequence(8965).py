_, *A = map(str.strip, open(0))
for a in A:
    n = len(a)
    print(min((2*a)[i:i+n]for i in range(n)))
