n = int(input())
x, y = '@ '
X, Y = x*n, y*n
A = [X+3*Y+X]*n+[X+2*Y+X]*n
print('\n'.join(A+[X*3]*n+A[::-1]))
