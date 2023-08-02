for l in open(0):
    print(int(eval(f"({'*('.join(l.split())}+.16)/.067)**.5")+.5))
