a, b, c = map(int, input().split(':'))
x, y, z = map(int, input().split(':'))
A = 3600*a+60*b+c
B = 3600*x+60*y+z
print(B-A if B-A > 0 else B-A+86400)
