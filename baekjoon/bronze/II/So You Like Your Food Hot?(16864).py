a, b, c = map(float, input().split())
i = j = 0
while b * i <= a:
    x = (a - (b * i))
    t = int(x // c)
    if x == t * c:
        j = 1
        print(i, t)
    i += 1
j or print('none')
