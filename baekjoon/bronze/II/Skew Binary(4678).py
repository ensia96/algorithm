while (A := input()[::-1]) != '0':
    x = 0
    print(sum(int(a)*(2**(x := x+1)-1)for a in A))
