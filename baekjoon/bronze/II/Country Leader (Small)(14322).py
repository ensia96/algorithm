I, R = input, range
for t in R(int(I())):
    print(f"Case #{t + 1}", sorted((-len({*(t := I())}), t)
          for _ in R(int(I())))[0][1])
