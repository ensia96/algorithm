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

# 신입 공채 당시에 제출했던 코드
#
# def solution(fees, records):
#     data_table = {}
#     st, sf, ut, uf = fees
#
#     for data in records:
#         time, car, action = data.split()
#         h, m = map(int, time.split(':'))
#
#     if car not in data_table:
#         data_table[car] = {'count': 0, 'record': [], 'fee': sf}
#         data_table[car]['record'] += [(action, (60*h)+m)]
#         data_table[car]['count'] += 1
#
#     _ = [data_table[data]['record'].append(('OUT', 1439))
#          for data in data_table if data_table[data]['count'] % 2]
#
#     for car in data_table:
#         data = data_table[car]
#         dummy = sorted(data['record'], key=lambda x: x[1])
#         in_data = [*filter(lambda x: x[0] == 'IN', dummy)]
#         out_data = [*filter(lambda x: x[0] == 'OUT', dummy)]
#         scope = len(in_data)
#         accumulate = sum(out_data[i][1] - in_data[i][1] for i in range(scope))
#         over = accumulate-st
#         extra = ((over)//ut+bool(over % ut))*uf if over > 0 else 0
#         data_table[car]['fee'] += extra
#
#     return [*map(lambda x: data_table[x]['fee'], sorted(data_table))]
