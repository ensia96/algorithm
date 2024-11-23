*A, b = open(0).read().split()
print(sum(a.startswith(b) and a != b for a in A))
