for _ in ' '*int(input()):
    n, A, B = int(input()), input(), input()
    w = b = 0
    for i in range(n):
        if A[i] != B[i]:
            w += A[i] == 'W'
            b += A[i] == 'B'
    print(max(w, b))
