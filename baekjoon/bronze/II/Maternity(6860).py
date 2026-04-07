A, B, _, *L = open(0).read().split()
for l in L:
    print(all((i in A) + (i in B) > (i > "Z")
          for i in l) * "Possible baby." or "Not their baby!")
