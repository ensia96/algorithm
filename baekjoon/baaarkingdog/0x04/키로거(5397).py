for _ in range(int(input())):
    p, n = [], []
    for c in input():
        if c not in "<>-":
            p.append(c)
        if p:
            if c == "<":
                n.append(p.pop())
            if c == "-":
                p.pop()
        if n and c == ">":
            p.append(n.pop())
    print("".join(p + n))
