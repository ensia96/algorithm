for l in [*open(0)][:-1]:
    a, b = map(int, l.split())
    print([["Undecided.", "Left beehind.", "To the convention."]
          [(a < b)+2*(a > b)], "Never speak again."][a+b == 13])
