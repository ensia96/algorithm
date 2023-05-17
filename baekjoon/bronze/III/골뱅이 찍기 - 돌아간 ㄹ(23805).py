n = int(input())
x, y = '@'*n, ' '*n
print('\n'.join([x*3+y+x]*n+[x+y+x+y+x]*3*n+[x+y+x*3]*n))
