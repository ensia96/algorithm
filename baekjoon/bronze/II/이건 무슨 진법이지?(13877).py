for _ in " " * int(input()):
    a, b = input().split()
    print(a, int(b, 8) if max(b) < "8" else 0, b, int(b, 16))
