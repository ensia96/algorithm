A = input()
print(max(sum(A.count(a) % 2 for a in {*A}), 1) - 1)
