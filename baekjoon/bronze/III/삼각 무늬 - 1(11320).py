for l in [*open(0)][1:]:
    print(sum(2*i+1 for i in range(eval(l.replace(' ', '//')))))
