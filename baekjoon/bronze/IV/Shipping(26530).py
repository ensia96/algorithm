for _ in ' '*int(input()):
    x = 0
    for _ in ' '*int(input()):
        _, a, b = input().split()
        x += float(a)*float(b)
    print(f'${x:.2f}')
