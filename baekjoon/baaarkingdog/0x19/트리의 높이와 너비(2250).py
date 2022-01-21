n = int(input())
n += 1
L, R, D, W, s = [0]*n, [0]*n, {}, [], 1
for _ in ' '*(n-1):
    c, l, r = map(int, input().split())
    L[c], R[c] = l, r


def F(s, l=1):
    if L[s] > 0:
        F(L[s], l+1)
    W.append(s)
    D[l] = D.get(l, [])+[len(W)]
    if R[s] > 0:
        F(R[s], l+1)


F(({*range(-1, n)}-{*(L+R)}).pop())
w, l = sorted((max(D[k])-min(D[k])+1, -k)for k in D).pop()
print(-l, w)
