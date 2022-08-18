import heapq as H
n = int(input())
A = []
for _ in ' '*n:
    _, s, e = map(int, input().split())
    H.heappush(A, (s, e))
Q, R = [], 0
while A:
    s, e = H.heappop(A)
    H.heappush(Q, e)
    while Q and Q[0] <= s:
        H.heappop(Q)
    R = max(R, len(Q))
print(R)
