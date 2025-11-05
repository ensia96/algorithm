l = input()
R = [[1, 5, 10, 50, 100, 500, 1000]['IVXLCDM'.index(i)]for i in l[1::2]]
print(sum(R[i] * int(l[i * 2]) * (1 - 2 * (i * 2 < len(l) -
      2 != R[i] < R[i + 1]))for i in range(len(l) // 2)))
