S = str
for i in open(0):
    print(*[sum(map(j, i[:-1]))
          for j in [S.islower, S.isupper, S.isdigit, S.isspace]])
