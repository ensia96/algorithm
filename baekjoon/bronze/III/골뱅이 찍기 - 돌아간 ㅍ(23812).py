n = int(input())
x, y = '@ '
X, Y = x*n, y*n
N = [X+3*Y+X]*n
print('\n'.join([*N, *[5*X]*n, *N, *[5*X]*n, *N]))
