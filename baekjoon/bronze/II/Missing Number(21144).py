n, A = open(i := 0)
for s in map(str, range(1, int(n)+1)):
    l = len(s)
    if A[i:i+l] != s:
        exit(print(s))
    i += l
