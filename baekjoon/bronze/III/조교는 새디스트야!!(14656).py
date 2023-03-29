input()
A = [*map(int, input().split())]
print(sum(A[i] != j for i, j in enumerate(sorted(A))))
