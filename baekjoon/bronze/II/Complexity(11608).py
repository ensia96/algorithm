A = input()
print(sum(sorted(map(A.count, {*A}))[:-2]))
