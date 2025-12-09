for l in [*open(0)][1:]:
    A = ''.join([[['', str(2 + sum(j < ord(i)for j in [67, 70, 73,
                76, 79, 83, 86]))][i.isupper()], i][i.isdigit()]for i in l])
    print(f"{A[:3]}-{A[3:6]}-{A[6:10]}")
