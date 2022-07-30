G = int(input())
f = l = r = 1
while l < G:
    t = r**2-l**2
    if t > G:
        l += 1
    else:
        if t == G:
            f = 0
            print(r)
        r += 1
f and print(-1)
