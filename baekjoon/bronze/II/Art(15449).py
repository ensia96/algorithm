A = [*map(int, input().split())]
x = 0
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(j + 1, 5):
            a, b, c = sorted([A[i], A[j], A[k]])
            x += a + b > c
print(x)
