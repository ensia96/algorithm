n, _ = map(int, input().split())
for a in input():
    x = 65 * a.isalpha() + 32 * a.islower()
    print(chr((ord(a) - x + n) % 26 + x) if x else a, end="")
