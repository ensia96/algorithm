D = {'P': 'R', 'R': 'S', 'S': 'P'}
for _ in ' '*int(input()):
    X = Y = 0
    for _ in ' '*int(input()):
        x, y = input().split()
        X += D[x] == y
        Y += D[y] == x
    print(*[['TIE'], ['Player', '12'[X < Y]]][(X > Y)+(X < Y)])
