n = int(input())
W = [0]
for _ in ' '*n:
    w = [*map(int, input().split())]
    W += w[0]+max(W[j]for j in w[2:]+[0]),
print(max(W))
