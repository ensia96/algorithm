s, b = [], {')': '(', ']': '['}

try:
    for i in input().replace('()', '2').replace('[]', '3'):
        if i in '([':
            s.append(i)
        elif i in ')]':
            v = 0
            while s[-1] != b[i]:
                d = s.pop()
                if type(d) != int:
                    raise Exception
                v += d
            s.append(v * (2 if s.pop() == '(' else 3))
        else:
            s.append(int(i))

    print(sum(s))
except:
    print(0)
