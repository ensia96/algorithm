A = input()
print(*(sum(map(int, A.replace(i, j).split()))
      for i, j in [['6', '5'], ['5', '6']]))
