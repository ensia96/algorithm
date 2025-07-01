for l in [*open(x := 0)][:-1]:
    a, b, c, d = map(int, l.split())
    for y in range(1, 21253):
        if y % 23 == a % 23 and y % 28 == b % 28 and y % 33 == c % 33:
            print(
                f"Case {(x:=x+1)}: the next triple peak occurs in {y-d} days.")
            break
