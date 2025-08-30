for l in [*open(0)][1:]:
    n, s, b, c = l.split()
    print(n, [['coach petitions', "ineligible"][int(c) > 40], "eligible"]
          [2009 < int(s.split('/')[0]) or int(b.split('/')[0]) > 1991])
