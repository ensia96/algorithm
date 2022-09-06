while 1:
    s = input()
    s == '.' and exit()
    n = len(s)
    f, j = [0]*n, 0
    for i in range(1, n):
        while j and s[i] != s[j]:
            j = f[j-1]
        if s[i] == s[j]:
            j += 1
            f[i] = j
    m = n-f[-1]
    print(1 if n % m else n//m)
