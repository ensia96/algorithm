import sys

sys.set_int_max_str_digits(10000000)
n, p = map(int, input().split())
t = str(n**p)
while t:
    print(t[:70])
    t = t[70:]
