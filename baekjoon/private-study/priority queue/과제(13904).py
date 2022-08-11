import heapq as H
n = int(input())
Q, l = [], 0
for _ in ' '*n:
    d, w = map(int, input().split())
    H.heappush(Q, (d, -w))
    l = max(l, d)
D = [-~l*[0]for _ in ' '*n]
for i in range(n):
    x, y = H.heappop(Q)
    for j in range(x):
        D[i][j] = max(D[i][j-1], D[i-1][j], D[i-1][j-1]-y)
print(max(D[-1]))
