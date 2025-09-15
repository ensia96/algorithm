A, B = open(0)
print("AN"[0 < len({*B} - {*A}) or sum(A.count(a) != B.count(a)
      for a in {*A}) > B.count('*')])
