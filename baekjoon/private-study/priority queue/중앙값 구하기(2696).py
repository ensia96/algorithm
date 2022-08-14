import heapq as H
I, D = H.heappush, H.heappop
for _ in ' '*int(input()):
    m = int(input())
    A, L, R, M = [], [], [], []
    for _ in ' '*(m//10+1):
        A += [*map(int, input().split())]
    for i in range(m):
        I(L, -A[i])if R and A[i] < R[0]else I(R, A[i])
        len(R) > len(L) and I(L, -D(R))
        len(L) > len(R) and I(R, -D(L))
        if i % 2 == 0:
            M += R[0],
    m //= 2
    print(m+1)
    x = 0
    for i in range(m//10+1):
        print(*M[x:x+10])
        x += 10
