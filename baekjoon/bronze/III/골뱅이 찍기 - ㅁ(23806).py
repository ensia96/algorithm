n = int(input())
x, y = '@ '
print('\n'.join([x*5*n]*n+[x*n+y*3*n+x*n]*3*n+[x*5*n]*n))
