import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
S, T, L = [], {1: []}, []
for _ in ' '*int(I()):
    h, k = map(int, I().split())
    i(S, (-h, k))
for h, k in S:
    for m in range(k-1, -1, -1):
        if T.get(m):
            d(T[m])
            T[m+1] = T.get(m+1, [])
            i(T[m+1], h)
            break
    else:
        T[1] += [h]
print(sum(map(lambda x: len(T[x]), T)))
