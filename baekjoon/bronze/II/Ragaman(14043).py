A, B = open(0)
print('NA'[sum((t := A.count(a) - B.count(a)) * (t > 0)
      for a in {*A}) == B.count('*')])
