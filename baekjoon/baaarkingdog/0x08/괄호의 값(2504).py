s, b, o, c, f = [], {')': '(', ']': '['}, '([', ')]', 1

try:
    for i in input().replace('()', '2').replace('[]', '3'):
        if not f:
            break
        if i in o:
            s.append(i)
        elif i in c:
            v = 0
            while s[-1] != b[i]:
                d = s.pop()
                if type(d) != int:
                    f = 0
                    break
                v += d
            s.append(v * (2 if s.pop() == '(' else 3))
        else:
            s.append(int(i))

    print(sum(s) if f else 0)
except:
    print(0)
