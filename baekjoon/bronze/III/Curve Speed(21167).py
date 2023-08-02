for l in open(0):
    print(eval(f"int(({'*('.join(l.split())}+.16)/.067)**.5)"))
