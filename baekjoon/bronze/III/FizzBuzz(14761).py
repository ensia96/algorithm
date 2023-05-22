x, y, n = map(int, input().split())
for i in range(1, n+1):
    X, Y = i % x < 1, i % y < 1
    print(['Fizz'*X+'Buzz'*Y, i][X+Y < 1])
