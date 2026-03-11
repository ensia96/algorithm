f=lambda v,d,k:k*v>0and v+f(v-d,d,k-1);a,b,c,d,_,*A=map(int,open(s:=0).read().split())
while A:x,y,*A=A;s+=max(f(a,b,x),f(c,d,y))
print(s)
