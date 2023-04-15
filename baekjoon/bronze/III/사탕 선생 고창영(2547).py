i, I = int, input
for _ in ' '*i(I()):
    I()
    x = i(I())
    print('YNEOS'[bool(sum(i(I())for _ in ' '*x) % x)::2])
