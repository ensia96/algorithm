n = int(input())
a, b, c = '*x '
for i in range(n*3):
    print([a*n+b*n+a*n, c*n+b*2*n, a*n+c*n+a*n][i//n])
