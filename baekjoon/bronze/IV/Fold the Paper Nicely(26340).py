for i in range(int(input())):
    i and print()
    *A, c = map(int, input().split())
    print('Data set:', *A, c)
    a, b = sorted(A)
    for _ in range(c):
        a, b = sorted([a, b//2])
    print(b, a)
