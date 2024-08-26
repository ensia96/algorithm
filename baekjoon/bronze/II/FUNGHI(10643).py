A = [*map(int, open(0))] * 2
print(max(sum(A[i : i + 4]) for i in range(8)))
