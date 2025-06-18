R = range(97)
for i in map(int, [*open(0)][:-1]):
    print(max((x := j**3+(k*-~k*-~-~k)//6)*(x <= i)for j in R for k in R))
