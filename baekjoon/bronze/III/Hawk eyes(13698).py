A = [1, 0, 0, 2]
for i in input():
    x, y = {'A': (0, 1), 'B': (0, 2), 'C': (0, 3),
            'D': (1, 2), 'E': (1, 3), 'F': (2, 3)}[i]
    A[x], A[y] = A[y], A[x]
print(A.index(1)+1, A.index(2)+1)
