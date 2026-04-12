_, r, *A = open(t := 0).read().split()
for a in A:
    x = int(r) - len(a)
    l = x + t >> 1
    print('.' * l + a + '.' * (x - l))
    t ^= x % 2
