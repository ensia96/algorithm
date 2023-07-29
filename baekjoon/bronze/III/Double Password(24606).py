A, B = open(0).read().split()
print(2**sum(a != b for a, b in zip(A, B)))
