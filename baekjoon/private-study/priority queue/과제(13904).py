import heapq as H
n = int(input())
Q = []
l = p = 0
for _ in ' '*n:
    d, w = map(int, input().split())
    H.heappush(Q, (-w, -d))
    l = max(l, d+1)
C = [1]*l
while Q:
    x, y = H.heappop(Q)
    while y:
        y += 1
        if C[y]:
            p -= x
            C[y] = 0
            break
print(p)
