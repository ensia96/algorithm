_,t,*A=map(int,open(0).read().split())
print(next((i+1for i,a in enumerate(A)if a<=t),'infinity'))
