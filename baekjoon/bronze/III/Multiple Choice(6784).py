n, *L = open(0)
n = int(n)
print(sum(L[i] == L[i+n]for i in range(n)))
