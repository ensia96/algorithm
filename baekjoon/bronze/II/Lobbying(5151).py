I = input
for D in range(int(I())):
    n, m, T = map(int, I().split())
    N = [0.] * n
    exec("i,t,d=I().split();N[int(i)-1]+=eval(d)*(-1<T-int(t)<1e3);" * m)
    N = [I() > 'N' or -1 / (1 + d / 1e4)for d in N]
    y = N.count(1)
    print('Data Set %d:\n%.2f %.2f\n' % (-~D, y, y - sum(N)))
