try:
    while 1:
        n = int(input())
        D = {}
        A = [input()for _ in ' '*n]
        V = 0
        for S in A:
            T = D
            for s in S:
                T[s] = T = T.get(s, {})
            T[0] = S
        for S in A:
            T = D
            for s in S:
                T[s] = T = T.get(s, {})
                V += len(T) > 1 or 0 in T
        print(f"{V/n:.2f}")
except:
    exit()
