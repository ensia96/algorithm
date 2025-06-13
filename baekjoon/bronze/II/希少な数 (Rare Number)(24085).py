*A, = map(int, [*open(0)][1].split())
print(min(A, key=lambda x: [A.count(x), x]))
