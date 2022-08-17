import heapq as H
n = int(input())
A = [(*map(int, input().split()),)for _ in ' '*n]
l, p = map(int, input().split())
Q = [(0, 0, p)]
f = 1
while Q:
    x, y, z = H.heappop(Q)
    if l <= y+z:
        f = 0
        break
    for i in range(n):
        a, b = A[i]
        y < a <= y+z and H.heappush(Q, (x+1, a, z-a+y+b))
print(-1 if f else x)
