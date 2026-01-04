i = 0
print(*[(i := a)for a in map(int, [*open(0).read().split()][1:])if i <= a])
