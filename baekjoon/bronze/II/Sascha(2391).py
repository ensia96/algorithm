for _ in ' '*int(input()):
    t, T = input(), []
    for j in range(int(input())):
        w = input()
        T += (sum(a != b for a, b in zip(t, w)), j, w),
    print(sorted(T)[0][2])
