i = 0
for l in [*open(0)][1:]:
    h, m = map(int, l.split())
    h, m = divmod(60*h+m-45, 60)
    i += 1
    print(f"Case #{i}:", h+24*(h < 0), m)
