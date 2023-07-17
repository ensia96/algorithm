print('JABCDEFGHIZ'[
      sum(x*y for x, y in zip(map(int, input()), (2, 7, 6, 5, 4, 3, 2))) % 11])
