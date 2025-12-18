*L, _ = open(0)
print(['PAY', 'PROTEST'][sum(eval(l.replace(*' *'))for l in L[1::2]) < int(_)])
