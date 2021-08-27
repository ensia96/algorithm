d = {'(': ')'}

for _ in range(int(input())):
    a, s = 0, []
    for i in input():
        if i in d:
            s.append(i)
        else:
            if not s:
                a = 1
                break
            s.pop()
    print('NO' if s or a else 'YES')
