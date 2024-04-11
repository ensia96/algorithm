a, b = int(input(), 2), int(input(), 2)
for i in [a & b, a | b, a ^ b]:
    print(bin(i).split('b')[1].rjust(10, '0'))
print(''.join('10'[int(i)]for i in bin(a)[2:]).rjust(10, '1'))
print(''.join('10'[int(i)]for i in bin(b)[2:]).rjust(10, '1'))
