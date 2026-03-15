*L,=map(int,open(0).read().split())
while L[0]:n,l,r,*L=L;print(sum(next((~i%2for i in range(n)if l%L[i]<1),~n%2)for l in range(l,r+1)));L=L[n:]
