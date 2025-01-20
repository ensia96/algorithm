n = int(input())
for a in [input() for _ in " " * n]:
    print("?", a)
    x = int(input())
    print("?", a)
    y = int(input())
    if x + y:
        exit(print("!", a))
