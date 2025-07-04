while (A := input()) != '#':
    t = 1
    x = (11-sum(i*(t := t+1)for i in map(int, A[::-1])) % 11) % 11
    print(A, '->', [x, 'Rejected'][x == 10])
