n = int(input())
A = sorted((*map(int, input().split()),)for _ in ' '*n)
D = [0]*501
for _, a in A:
    D[a] = max(D[:a])+1
print(n-max(D))
