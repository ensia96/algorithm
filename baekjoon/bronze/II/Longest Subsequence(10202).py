for l in [*open(0)][1:]:
    c = 0
    print("The longest contiguous subsequence of X's is of length",
          max(c := -~c*(i == 'X')for i in l.split()))
