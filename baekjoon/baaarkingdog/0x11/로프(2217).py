n, *l = map(int, open(0))
l = sorted(l)
print(max(l[i]+l[i]*(n-i-1)for i in range(n)[::-1]))
