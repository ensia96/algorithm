n,*A=map(int,open(0).read().split())
t=sum(a%2for a in A)*2<n
while-~t in A:t+=2
print(-~t)
