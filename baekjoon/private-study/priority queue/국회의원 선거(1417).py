import heapq as H
n = int(input())
A = [0]*n
Q = []
c = 0
for i in range(n):
    A[-i] = -int(input())
    H.heappush(Q, (A[-i], -i))
while 1:
    x, y = H.heappop(Q)
    if not y and x == A[0]:
        break
    A[y] += 1
    A[0] -= 1
    c += 1
    H.heappush(Q, (A[y], y))
    H.heappush(Q, (A[0], 0))
if Q and x > Q[0][0]:
    c += 1
print(c)
