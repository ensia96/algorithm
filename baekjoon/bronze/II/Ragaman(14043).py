A, B = open(0)
print("AN"[sum(A.count(a) > B.count(a)for a in {*A}) > B.count('*')])
