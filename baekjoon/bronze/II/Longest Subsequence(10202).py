for l in [*open(0)][1:]:
    _, *A = l.split()
    x = y = 0
    for a in A:
        x = [0, x+1][a == 'X']
        y = max(y, x)
    print("The longest contiguous subsequence of X's is of length", y)
