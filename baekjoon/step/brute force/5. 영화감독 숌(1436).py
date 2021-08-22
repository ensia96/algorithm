c, n = 0, int(input())
for i in range(int(10e9)):
    if '666' in str(i):
        c += 1
    if c == n:
        print(i)
        exit()
