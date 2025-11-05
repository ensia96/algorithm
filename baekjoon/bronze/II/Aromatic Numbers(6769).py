l = input()
R = [[1, 5, 10, 50, 100, 500, 1000]['IVXLCDM'.index(i)]for i in l[1::2]]
t = len(l)
print(sum(R[i] * int(l[i * 2]) * (1 - 2 * (i * 2 < t - 2 != R[i] < R[i + 1]))
      for i in range(t // 2)))
