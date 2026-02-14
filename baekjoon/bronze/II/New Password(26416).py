for l in [*open(t := 0)][2::2]:
    l = l[:-1]
    t += 1
    l += "A"[l < l.lower():] + "a"[l > l.upper():] + \
        "0"[any(map(str.isdigit, l)):] + "#"[len({*l} & {*"#@*&"}):]
    print(f"Case #{t}: {l:a<7}")
