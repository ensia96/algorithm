n, *L = map(int, open(0).read().split())
print([sum(L[2*i+1]-L[2*i]for i in range(n//2)), 'still running'][n % 2])
