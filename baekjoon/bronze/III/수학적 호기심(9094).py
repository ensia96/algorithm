for l in [*open(0)][1:]:
    n, m = map(int, l.split())
    print(sum(not ((i*i+j*j+m)/(i*j) % 1)
          for i in range(1, n)for j in range(i+1, n)))
