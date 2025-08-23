n, *L = map(str.strip, open(0))
while n := int(n):
    print(*map(sum, zip(*[[l in 'ML', (x := l.isdigit()) and int(l)
          > 11, x and int(l) < 12, l == 'S', l == 'X']for l in L[:n]])))
    n, *L = L[n:]
