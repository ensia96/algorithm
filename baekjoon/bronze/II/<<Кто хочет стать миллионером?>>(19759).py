a = 50
for _ in ' ' * int(input()):
    t = a = a * 2
    x = 0
    while t % 10 < 1:
        t //= 10
        x += 1
    print(a := [a, -(t // -10) * 10**-~x][len(str(a)) > x * 2])
