_, *A = open(0).read().split()
t = 0
for a in A:
    m, s = map(int, a.split(':'))
    t += 60*m+s
print(f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}")
