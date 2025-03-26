import sys

sys.set_int_max_str_digits(10000000)
n, p = map(int, input().split())
while t := str(n**p):
    print(t[:70])
    t = t[70:]
