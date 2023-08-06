*A, = map(int, open(0).read().split()[:-1])
while A:
    n, x, y, *A = A
    for _ in ' '*n:
        i, j, *A = A
        t = ['', 'S', 'N'][(y > j)+2*(y < j)]+['', 'O', 'E'][(x > i)+2*(x < i)]
        print([t, 'divisa'][len(t) < 2])
