n = int(input())
x, y = '@'*n, ' '*n
X, Y = x+y*3+x, x*5
print('\n'.join([X]*2*n+[Y]*n+[X]*n+[Y]*n))
