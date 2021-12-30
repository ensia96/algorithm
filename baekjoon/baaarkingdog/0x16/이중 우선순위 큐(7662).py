import heapq as h
for _ in ' '*int(input()):
    Q, k = [], int(input())
    for _ in ' '*k:
        o, n = input().split()
        n = int(n)
        if o == 'I':
            h.heappush(Q, n)
        elif Q:
            h.heappop(Q) if n < 0 else Q.pop()
    print(Q and f"{max(Q)} {min(Q)}" or 'EMPTY')
