for l in [*open(0)][1:]:
    n = int(l)
    print(f'Pairs for {n}:', ', '.join(
        f'{i+1} {n+~i}'for i in range(n//2+n % 2-1)))
