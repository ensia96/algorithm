n = int(input())
A = [float(input())for _ in ' '*n]
D = [A[0]]
for i in range(1, n):
    D += max(D[-1]*A[i], A[i]),
print(f"{max(D):.3f}")
