import heapq as h
for _ in ' '*int(input()):
    Q, k = [], int(input())
    for _ in ' '*k:
        o, n = input().split()
        n = int(n)
        if o == 'I':
            h.heappush(Q, n)
        elif len(Q):
            h.heappop(Q) if n < 0 else Q.pop()
    print(Q and f"{Q[-1]} {Q[0]}" or 'EMPTY')
