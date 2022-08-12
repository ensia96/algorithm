import heapq as H
k, n = map(int, input().split())
A = [*map(int, input().split())]
Q = [1]
C = set([1])
M = 0
while n:
    x = H.heappop(Q)
    for a in A:
        t = a*x
        if t in C or len(Q) > n and M <= t:
            continue
        H.heappush(Q, t)
        M = max(M, t)
        C.add(t)
    n -= 1
print(Q[0])
