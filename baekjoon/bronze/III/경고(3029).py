a, b, c = map(int, input().split(':'))
x, y, z = map(int, input().split(':'))
A = (60*(x-a)+y-b)*60+z-c
print(f'{A//3600+24*(A<=3600):02d}:{A//60%60:02d}:{A%60:02d}')
