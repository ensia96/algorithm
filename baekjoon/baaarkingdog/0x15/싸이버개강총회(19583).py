t, *C = open(0)
s, e, q = (int(t.replace(':', ''))for t in t.split())
A = {}
for l in C:
    t, n = l.split()
    t, a = int(t.replace(':', '')), A.get(n, [0, 0])
    A[n] = [a[0] or t <= s, a[1] or e <= t <= q]
print(sum(all(A[n])for n in A))
