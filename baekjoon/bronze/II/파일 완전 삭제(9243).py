n, a, b = open(0).read().split()
a, b = int(a, 2), int(b, 2)
print('Deletion', ['failed', 'succeeded'][[a == b, not (a & b)][int(n) % 2]])
