'''
_, *L = map(int, open(0).read().split())
while L:
    n, e, *L = L
    N = [*range(n)]
    for i in L[:e]:
        N = [N.pop(N.index(i - 1))] + N
    print(N[-1] + 1)
    L = L[e:]
'''
_,*L=map(int,open(0).read().split())
while L:
 n,e,*L=L
 N=[*range(1,n+1)]
 for i in L[:e]:N.remove(i);N=[i]+N
 print(N[-1]);L=L[e:]
