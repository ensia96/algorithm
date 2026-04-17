while(n:=int(input())):print(sum((n-k*~-k//2)%k<1for k in range(2,n+2)if k*~-k<=n*2))
