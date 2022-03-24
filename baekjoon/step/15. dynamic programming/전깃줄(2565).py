n = int(input())
T = sorted((*map(int, input().split()),)for _ in ' '*n)
_, A = zip(*T)
D = [0]*501
for a in A:
    D[a] = max(D[:a])+1
print(n-max(D))
