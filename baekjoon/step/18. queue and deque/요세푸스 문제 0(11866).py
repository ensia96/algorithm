import collections
n, k = map(int, input().split())
A = collections.deque(map(str, range(1, n+1)))
R = []
while A:
    A.rotate(-k)
    R += A.pop(),
print('<'+', '.join(R)+'>')
