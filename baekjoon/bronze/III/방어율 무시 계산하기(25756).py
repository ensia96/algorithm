n, *A = map(int, open(0).read().split())
x = 0
for a in A:
    x = (100*(a+x)-a*x)/100
    print(x)
