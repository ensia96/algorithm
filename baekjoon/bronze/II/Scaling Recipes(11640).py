for t in range(int(input())):
    print('Recipe #', t + 1)
    R, P, D = map(int, input().split())
    I = [input().split()for _ in '_' * R]
    x, = [eval(w) * D / P for n, w, p in I if p == '100.0']
    [print(n, x * eval(p) / 100)for n, w, p in I]
    print('-' * 40)
