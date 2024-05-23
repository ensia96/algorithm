n, k, l, *A = map(int, open(0).read().split())
T = []
for i in range(n):
    t = A[i*3:i*3+3]
    if not (l > min(t) or sum(t) < k):
        T += t
print(len(T)//3)
print(*T)
