for l in [*open(0)][:-1]:
    print(sum((ord(l[i])-64)*-~i*(l[i].isalpha())for i in range(len(l))))
