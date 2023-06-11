for l in [*open(0)][:-1]:
    a, b = l.split()
    h, m = map(int, a.split(':'))
    H, M = map(int, b.split(':'))
    T = 60*h+m+60*H+M
    d = T//60//24
    print(f'{T//60%24:02d}:{T%60:02d}', f'+{d}'if d else '')
