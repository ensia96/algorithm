for l in [*open(0)][:-1]:
    print(l[:-3] + ['or', 'our'][5 < len(l)
          and l[:-1].endswith('or') and l[-4]not in 'aeiouy'])
