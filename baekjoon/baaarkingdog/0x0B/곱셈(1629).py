def s(a, b, c):
    if b == 1:
        return a % c
    d = s(a, b//2, c)
    d = d**2 % c
    return d*a % c if b % 2 else d


print(s(*map(int, input().split())))
