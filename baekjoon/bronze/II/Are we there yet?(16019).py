A = [0, *map(int, input().split())]
B = [5 * [0] for _ in " " * 5]
for i in range(5):
    for j in range(i + 1, 5):
        B[i][j] = B[j][i] = sum(A[i : j + 1]) - A[i]
for b in B:
    print(*b)
