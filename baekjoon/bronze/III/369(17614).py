print(sum(sum(map(lambda x: x in '369', str(i+1)))
      for i in range(int(input()))))
