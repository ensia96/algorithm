_, A, B = open(0)
print(sum(max(B.count(b) - A.count(b), 0)for b in {*B}))
