for l in [*open(t := 0).read().split()][2::2]:
    x, *A = map(int, l)
    y = 0
    for i in range(len(A)):
        if i+1 > x:
            y += i+1-x
            x += i+1-x
        x += A[i]
    print(f"Case #{(t:=t+1)}:", y)
