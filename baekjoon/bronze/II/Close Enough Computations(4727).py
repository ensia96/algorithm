while 0 < sum(A := [*map(int, input().split())]):
    C, f, c, p = A
    print('yneos'[int((f * 9 + (c + p) * 4 + 5) / 10) * 10 != C::2])
