n, *A = map(int, open(0).read().split())
x, y = map(sum, zip(*[(a > b, b > a)for a in A[:n]for b in A[n:]]))
print(['tie', 'first', 'second'][(x > y)+2*(x < y)])
