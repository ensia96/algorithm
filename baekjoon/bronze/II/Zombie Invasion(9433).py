for l in [*open(0)][1:]:
    L = l.split()
    a = 0
    T = []
    exec("a+=int(L.pop());T=[a%2]+T;a//=2;" * 20)
    T[0] += a * 2
    print(*T)
