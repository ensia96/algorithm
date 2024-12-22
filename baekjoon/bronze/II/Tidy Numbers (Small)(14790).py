f = lambda x: [*str(x)] == sorted(str(x))
for l in [*open(t := 0)][1:]:
    t += 1
    print(
        f"Case #{t}:",
        (
            y
            if f(y := int(l))
            else [
                x
                for i in range(len(l) - 1)
                if f(x := int(str(int(l[: -i - 1]) - 1) + "9" * i))
            ][0]
        ),
    )
