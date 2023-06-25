for i in range(int(input())):
    x = y = 1000
    X = Y = -1000
    for _ in ' '*int(input()):
        a, b = map(float, input().split())
        x = min(a, x)
        y = min(b, y)
        X = max(a, X)
        Y = max(b, Y)
    print(f'Case {i+1}: Area {(X-x)*(Y-y)}, Perimeter {2*(X-x)+2*(Y-y)}')
