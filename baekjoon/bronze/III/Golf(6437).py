x = 1
while 1:
    p, s = map(int, input().split())
    if p == s == 0:
        break
    y = p-s
    print(f"Hole #{x}")
    if s == 1:
        print("Hole-in-one.")
    elif y == 3:
        print("Double eagle.")
    elif y == 2:
        print("Eagle.")
    elif y == 1:
        print("Birdie.")
    elif y == 0:
        print("Par.")
    elif y == -1:
        print("Bogey.")
    else:
        print("Double Bogey.")
    print()
    x += 1
