import heapq as H
n, l = map(int, input().split())
i, Q, R = 0, [], []
for a in map(int, input().split()):
    H.heappush(Q, (a, i))
    while Q:
        x, y = H.heappop(Q)
        if i-l+1 <= y:
            H.heappush(Q, (x, y))
            R += x,
            break
    i += 1
print(*R)
