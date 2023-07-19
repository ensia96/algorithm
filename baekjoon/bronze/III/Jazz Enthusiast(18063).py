n, c = map(int, input().split())
A = -~-n*c
for _ in ' '*n:
    m, s = map(int, input().split(':'))
    A += m*60+s
print(f'{A//3600:02}:{A%3600//60:02}:{A%60:02}')
