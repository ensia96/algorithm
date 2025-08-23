n, *L = map(str.strip, open(0))
while n := int(n):
    print(*map(sum, zip(*[[l in 'ML', '11' < l < 'A',
          l < '12', l == 'S', l == 'X']for l in L[:n]])))
    n, *L = L[n:]
