_, A, B = map(str.split, open(0))
print(sum(a in B for a in A))
