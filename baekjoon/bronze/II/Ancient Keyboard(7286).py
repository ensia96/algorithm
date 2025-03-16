x = 1001
for _ in " " * int(input()):
    n = int(input())
    A = [0] * x
    for _ in " " * n:
        t, a, b = input().split()
        a, b = int(a), int(b)
        for i in range(a, b):
            A[i] += 1
    print(*[chr(64 + A[i]) for i in range(x) if A[i]], sep="")
