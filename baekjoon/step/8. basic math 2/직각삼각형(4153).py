a = True

while a:
    l = list(map(int, input().split()))
    l.sort()

    a, b, c = l

    if not a:
        break

    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")
