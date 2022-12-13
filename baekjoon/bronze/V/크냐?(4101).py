while 1:
    a, b = map(int, input().split())
    if a*b:
        print("YNeos"[a <= b::2])
    else:
        break
