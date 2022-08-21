import heapq as H
n, k = map(int, input().split())
Q, A, C, x = [], [], [0]*k, 0
for _ in ' '*n:
    i, w = map(int, input().split())
    if len(Q) == k:
        x, y, z = Q[0]
        while Q and Q[0][0] == x:
            a, b, c = H.heappop(Q)
            C[-b] = 0
            A += c,
    for c in range(k):
        if not C[c]:
            C[c] = 1
            H.heappush(Q, (x+w, -c, i))
            break
while Q:
    A += H.heappop(Q)[2],
print(sum(-~i*A[i]for i in range(n)))
