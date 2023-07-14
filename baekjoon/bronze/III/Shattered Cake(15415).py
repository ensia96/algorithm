w, n, *L = map(int, open(0).read().split())
print(sum(L[2*i]*L[2*i+1]for i in range(n))//w)
