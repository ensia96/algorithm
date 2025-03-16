x = 1001
for _ in " " * int(input()):
    n = int(input())
    A = [0] * x
    for _ in " " * n:
        for i in range(*map(int, input().split()[1:])):
            A[i] += 1
    print(*[chr(64 + A[i]) for i in range(x) if A[i]], sep="")
