L, A = lambda: map(int, input().split()), input()
R, P = [*L()], [*L()][:-1]
y = R.pop()
A = y*P.pop()
while R:
    x, s = R.pop(), P.pop()
    y += x
    A = min(A+s*x, s*y)
print(A)
