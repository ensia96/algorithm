M = 60
a, b = open(0).read().split()
h, m = map(int, a.split(':'))
b = int(b)-(m % 15 < 1)-(m < 1)*~-h
while b > 0:
    m = (m+15-m % 15) % M
    h = (h+(m < 1)) % 13 or 1
    b -= (m > 0)+(m < 1)*h
print(f"{h:02}:{m:02d}")
