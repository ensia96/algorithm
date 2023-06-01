a, b, c = map(int, input().split(':'))
x, y, z = map(int, input().split(':'))
t = 60*(60*(x-a)+y-b)+z-c
print(f"{t//3600+24*(t<=0):02d}:{t//60%60:02d}:{t%60:02d}")
