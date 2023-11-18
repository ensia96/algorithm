a, b = input(), input()
h, m = map(int, b.split(':'))
T = h*60+m+1440
h, m = map(int, a.split(':'))
T -= h*60+m
print(f'{T//60:02d}:{T%60:02d}')
