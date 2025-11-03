while 0 < sum(A := [*map(int, input().split())]):
    C, f, c, p = A
    print('yneos'[round((f * 9 + (c + p) * 4 + 1) / 10) * 10 != C::2])
