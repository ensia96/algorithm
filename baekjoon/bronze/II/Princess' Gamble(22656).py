while sum(A := [*map(int, input().split())]):
    n, m, p = A
    X = eval("int(input())," * n)
    print(X[m - 1] and sum(X) * (100 - p) // X[m - 1])
