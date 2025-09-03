import math
n = int(input())
x = 10**int(math.log10(n))
print(round(n / x) * x)
