f = lambda x: sum(map(int, str(x)))
while n := int(input()):
    t = 11
    while f(n) != f(n * t):
        t += 1
    print(t)
