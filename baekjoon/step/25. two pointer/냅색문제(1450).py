import sys

n, c = map(int, sys.stdin.readline().split())
W = list(map(int, sys.stdin.readline().split()))
aw = W[:n // 2]
bw = W[n // 2:]
asum = []
bsum = []


def F(W, S, l, w):
    if l >= len(W):
        S.append(w)
        return
    F(W, S, l + 1, w)
    F(W, S, l + 1, w + W[l])


def B(A, t, s, e):
    while s < e:
        mid = (s + e) // 2
        if A[mid] <= t:
            s = mid + 1
        else:
            e = mid
    return e


F(aw, asum, 0, 0)
F(bw, bsum, 0, 0)
bsum.sort()

cnt = 0
for i in asum:
    if c - i < 0:
        continue
    cnt += B(bsum, c - i, 0, len(bsum))
print(cnt)
