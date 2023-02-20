x, y = 'double', int(input())
for i in range(y):
    a, b, c = map(int, input().split())
    print(a, b, c)
    z = (a > 9)+(b > 9)+(c > 9)
    print(['zlich', x, x+'-'+x, 'triple-'+x][z])
    (i < y-1) and print()
