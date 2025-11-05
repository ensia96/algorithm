l = input()
R = [[1, 5, 10, 50, 100, 500, 1000]['IVXLCDM'.index(i)]for i in l[1::2]]
print(sum(int(l[2 * i]) * R[i] * (1 - 2 * (2 * -~i < len(l)
      and R[i] < R[i + 1]))for i in range(len(l) // 2)))
