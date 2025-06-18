for i in map(int, [*open(0)][:-1]):
    print(max(x for j in range(54)
          for k in range(97)if (x := j**3+(k*-~k*-~-~k)//6) <= i))
