while (A := input()) != '#':
    print(([t for i in range(len(A))if (t := A[:i]+A[i+1:])
          == t[::-1]] or ['not possible'])[0])
