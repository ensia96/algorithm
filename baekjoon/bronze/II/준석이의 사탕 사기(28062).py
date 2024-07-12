_, *A = map(int, open(0).read().split())
print(sum(A) - len(t := [a for a in A if a % 2]) % 2 * min(t + [1000]))
