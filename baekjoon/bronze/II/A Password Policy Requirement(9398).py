for l in [*open(0)][1:]:
    print(min([j - i for i in range(len(l))for j in range(i + 6, len(l))
          if all(any(map(f, l[i:j]))for f in [str.isdigit, str.islower, str.isupper])] or [0]))
