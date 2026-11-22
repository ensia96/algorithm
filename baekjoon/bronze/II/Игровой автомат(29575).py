n,*a=open(0);n=int(n);d=dict(map(str.split,a[:n]))
print(sum(int(d.get(x[:4],0))-10for x in a[n+1:]))
