for l in [*open(0)][1:]:
    print('TF'[sum(sum(map(int, str(int(l[i])*(2-i % 2))))
          for i in range(16)) % 10 > 0])
