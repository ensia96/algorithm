n, *L = open(t := 0)
while L:
    l, *L = L
    l = int(l)
    J, L = L[:l], L[l:]
    t += 1
    print(f"Case {t}:", ['Standing', 'Fallen'][any('00' in j for j in J)])
