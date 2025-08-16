for c in map(int, [*open(0)][1:]):
    print(2*min(w*h+c//w//h*(w+h)for w in range(1, c+1)
          for h in range(1, c//w+1)if not c % (w*h)))
