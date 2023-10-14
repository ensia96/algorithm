for n in map(int, open(0).read().split()[1:]):
    print(sum(-~i*(n-i)for i in range(n)))
