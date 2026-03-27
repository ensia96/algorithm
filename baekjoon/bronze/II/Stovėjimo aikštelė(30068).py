D = {}
exec(
    't,n=map(int,input().split());n in D and print(n,t-D[n]);D[n]=t;' * int(input()))
