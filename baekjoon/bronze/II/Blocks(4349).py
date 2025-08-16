for c in map(int, [*open(0)][1:]):
    print(min(2*((i+j)*c//(i*j)+(i*j))for i in range(1, int(c**.5)+1)
          for j in range(1, c//i+1)if not c % (i*j)))
