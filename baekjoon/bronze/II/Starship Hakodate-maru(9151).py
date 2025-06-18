R = range(97)
while i := int(input()):
    print(max((x := j**3+k*~k*~-~k//6)*(x <= i)for j in R for k in R))
