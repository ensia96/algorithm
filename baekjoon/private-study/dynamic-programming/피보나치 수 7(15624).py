a, b = 0, 1
for M in [1000000007]*int(input()):
    a, b = b % M, a+b
print(a)
