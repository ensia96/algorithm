I = input
while '$' < (A := I()):
    l, n = A.split()
    n = int(n)
    c = int(I())
    for _ in ' ' * int(I()):
        a, b = map(int, I().split())
        c = min(n, c - a + b)
    print(l, c)
