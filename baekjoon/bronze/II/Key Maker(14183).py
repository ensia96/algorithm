while (A := input()) != "0 0":
    m, n = map(int, A.split())
    (*A,) = map(int, input().split())
    print(
        sum(all(i >= j for i, j in zip(A, map(int, input().split()))) for _ in " " * n)
    )
