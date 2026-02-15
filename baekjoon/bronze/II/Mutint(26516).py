while (i := input()) > '0':
    print(int(i[:(x := i.find(max(i)))] +
          str([n := int(i[x]) + 4, 0][n % 2] % 10) + i[x + 1:]))
