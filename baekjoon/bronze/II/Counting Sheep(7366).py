for l in [*open(t := 0)][2::2]:
    t += 1
    print(f"Case {t}: This list contains {l.split().count('sheep')} sheep.\n")
