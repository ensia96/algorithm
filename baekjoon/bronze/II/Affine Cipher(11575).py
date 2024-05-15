I = input
for i in range(int(I())):
    a, b, = map(int, I().split())
    print(''.join(chr((a*(ord(i)-65)+b) % 26+65)for i in I()))
