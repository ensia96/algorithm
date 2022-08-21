from heapq import *
n, k = map(int, input().split())
Q, A, C, x = [], [0], [*range(k)], 0
heapify(C)
for _ in ' '*n:
    i, w = map(int, input().split())
    if len(Q) == k:
        x = Q[0][0]
        while Q and Q[0][0] == x:
            a, b, c = heappop(Q)
            heappush(C, -b)
            A += c*len(A),
    heappush(Q, (x+w, -heappop(C), i))
while Q:
    A += heappop(Q)[2]*len(A),
print(sum(A))
