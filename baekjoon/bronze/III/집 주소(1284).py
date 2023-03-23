for l in [*open(0)][:-1]:
    print(sum(4-(i == '1')+(i == '0')for i in l)-3)
