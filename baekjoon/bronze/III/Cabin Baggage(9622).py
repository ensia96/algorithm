x = 0
for l in [*open(0)][1:]:
    a, b, c, d = map(float, l.split())
    y = bool((a <= 56)*(b <= 45)*(c <= 25)+(a+b+c <= 125))*(d <= 7)
    print(y)
    x += y
print(x)
