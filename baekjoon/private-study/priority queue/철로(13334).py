import heapq as H
n = int(input())
A = [sorted(map(int, input().split()))for _ in ' '*n]
d = int(input())
Q, S, T, R = [], [], [], 0
while A:
    x, y = A.pop()
    y <= x+d and H.heappush(Q, (x, y))
while Q:
    x, y = H.heappop(Q)
    H.heappush(S, (x, y))
    while Q:
        a, b = H.heappop(Q)
        H.heappush(S, (a, b))if b <= x+d else H.heappush(T, (a, b))
    R = max(R, len(S))
    for x, y in T:
        H.heappush(Q, (x, y))
    T = []
    while S and Q and S[0][0] < Q[0][0]:
        H.heappop(S)
print(R)
