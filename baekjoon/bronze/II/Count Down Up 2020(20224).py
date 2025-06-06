for l in [*open(0)][1::2]:
    print(sum(l[i:i+7] == '2 0 2 0'for i in range(len(l))))
