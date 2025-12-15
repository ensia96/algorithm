A, *L = open(0)
L = [''.join('XYG'[2 * (A[i] == l[i]) or l[i] in A]
             for i in range(5))for l in L]
print(*L[:L.index('GGGGG')if (A := 'GGGGG' in L)else -1],
      'WLIONSNEERR'[1 - A::2])
