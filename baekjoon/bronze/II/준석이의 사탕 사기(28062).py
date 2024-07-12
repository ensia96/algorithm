_, *A = map(int, open(0).read().split())
print(sum(A) - sum((t := [a for a in A if a % 2])[: len(t) % 2]))
