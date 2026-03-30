_, *L = map(int, open(t := 0).read().split())
while L:
    n, *L = L
    x = y = 0
    exec("a,b,*L=L;x+=a*(a-b>1)+(a+b)*-~(b==2)*(b-a==1);y+=b*(b-a>1)+(a+b)*-~(a==2)*(a-b==1);" * n)
    t += 1
    print(f'Game {t}: Tessa {x} Danny {y}')
