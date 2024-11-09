for l in [*open(i := 0)][1:]:
    i += 1
    print(f"Case #{i}:", *l.split()[::-1])
