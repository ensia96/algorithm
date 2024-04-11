a, b = int(input(), 2), int(input(), 2)
n = 100000
m = 2**n-1
for i in [a & b, a | b, a ^ b, a ^ m, b ^ m]:
    print(bin(i).split('b')[1].rjust(n, '0'))
