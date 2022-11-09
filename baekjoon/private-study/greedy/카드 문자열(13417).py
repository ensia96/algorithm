for _ in ' '*int(input()):
    input()
    a, *A = input().split()
    for i in A:
        a = a+i if a[0] < i else i+a
    print(a)
