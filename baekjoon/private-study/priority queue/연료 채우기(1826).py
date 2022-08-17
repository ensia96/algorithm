import heapq as H
n = int(input())
A = [(*map(int, input().split()),)for _ in ' '*n]
H.heapify(A)
l, p = map(int, input().split())
Q = []
a = 0
while p < l:
    while A and A[0][0] <= p:
        H.heappush(Q, -H.heappop(A)[1])
    Q or exit(print(-1))
    p -= H.heappop(Q)
    a += 1
print(a)
