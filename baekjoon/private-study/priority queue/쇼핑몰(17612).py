import heapq as H
n, k = map(int, input().split())
Q, A, C, x = [], [], [*range(k)], 0
H.heapify(C)
for _ in ' '*n:
    i, w = map(int, input().split())
    if len(Q) == k:
        x, y, z = Q[0]
        while Q and Q[0][0] == x:
            a, b, c = H.heappop(Q)
            H.heappush(C, -b)
            A += c,
    H.heappush(Q, (x+w, -H.heappop(C), i))
while Q:
    A += H.heappop(Q)[2],
print(sum(-~i*A[i]for i in range(n)))
