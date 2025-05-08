i = input
for _ in ' '*int(i()):
    t, T = i(), []
    for j in range(int(i())):
        w = i()
        T += (sum(a != b for a, b in zip(t, w)), j, w),
    print(sorted(T)[0][2])
