def solution(fees, records):
    T = {}

    for r in records:
        t, c, f = r.split()
        h, m = map(int, t.split(':'))
        t, c, f = h*60+m, int(c), f == 'IN'
        T[c] = T.get(c, [])+[t]

    for c in T:
        t = 0
        if len(T[c]) % 2:
            T[c] += [1439]
        while T[c]:
            o, i = T[c].pop(), T[c].pop()
            t += o-i
        t, A = t-fees[0], fees[1]
        A += (t > 0)*fees[3]*(t//fees[2]+bool(t % fees[2]))
        T[c] = A

    return [T[c]for c in sorted(T)]
