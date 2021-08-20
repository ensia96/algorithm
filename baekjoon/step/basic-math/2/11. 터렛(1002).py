for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            break
        print(0)
        break

    l = (x1 - x2) ** 2 + (y1 - y2) ** 2
    r = (r1 + r2) ** 2

    print(0 if l > r else 2 if l < r else 1)
