import bisect as B
n, h = map(int, input().split())
A, f, c = [[], []], B.bisect_left, n//2
for i in range(n):
    A[i % 2] += int(input()),
A[0].sort()
A[1].sort()
T = [c-f(A[0], i+1)+c-f(A[1], h-i)for i in range(h)]
print(min(T), T.count(min(T)))
