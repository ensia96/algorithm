k, m = int(input()), 210
for _ in ' '*int(input()):
    t, z = input().split()
    m -= int(t)
    m < 0 and exit(print(k))
    k = max((k+(z == 'T')) % 9, 1)
