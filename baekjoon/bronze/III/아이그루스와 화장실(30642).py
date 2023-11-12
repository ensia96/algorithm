n, b, k = open(0).read().split()
n, k = int(n), int(k)
print(k-[(k % 2)-2*(k == 1), not k % 2]['a' in b])
