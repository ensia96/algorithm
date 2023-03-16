for _ in ' '*int(input()):
    a, b = map(int, input().split())
    A = B = C = 0
    x, y = 10, 1
    for i in range(6):
        A += i+1
        B += 2**i
        if A > a:
            C += [50, 30, 20, 5, 3, 1][i]*x
            x = 0
        if B > b:
            C += [512, 256, 128, 64, 32, 0][i]*y
            y = 0
    print(C*10000)
