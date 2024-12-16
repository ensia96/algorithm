for l in open(0):
    print("yneos"[("problem" in l.lower()) ^ 1 :: 2])
