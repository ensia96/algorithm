for l in [*open(0)][1:]:
    _, *l = map(int, l.split())
    _, *t = {j - i for i, j in zip(l, l[1:])}
    print(*[["The next 5 numbers after", l, "are:", [-~i * _+l[-1]for i in range(5)]],
          ["The sequence", l, "is not an arithmetic sequence."]][len(t) > 0])
