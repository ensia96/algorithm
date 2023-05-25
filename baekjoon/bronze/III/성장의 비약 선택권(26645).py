n = int(input())
print(max((max(min(8, 209-n), 0), 1), (max(min(4, 219-n), 0), 2),
      (max(min(2, 229-n), 0), 3), (0, 4))[1])
