a, b, c, d = map(int, open(t := 0))
R = range(101)
for i in R:
    for j in R:
        for k in R:
            if 0 < (a * i + b * j + c * k) <= d:
                print(i, "Brown Trout,", j, "Northern Pike,", k, "Yellow Pickerel")
                t += 1
print("Number of ways to catch fish:", t)
