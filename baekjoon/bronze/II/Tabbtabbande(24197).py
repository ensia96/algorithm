n,_,*A=map(int,open(0).read().split());p=1
print(sum(min(x:=abs(p-(p:=a)),n-x)for a in A))
