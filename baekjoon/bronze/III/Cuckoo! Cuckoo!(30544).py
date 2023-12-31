M = 60
a, b = open(0).read().split()
h, m = map(int, a.split(':'))
T = h*M+m-1
b = int(b)
while b > 0:
    b -= 1+(T % M < 1)*(T//M-1)
    T += 15-T % 15
print(f"{T//M%12 or 12:02d}:{T%M:02d}")
