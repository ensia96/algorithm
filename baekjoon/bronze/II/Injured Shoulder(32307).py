n, *a = open(0)
n = int(n)
for i in a[n + 1:]:
    print(+(i in a[:n])
          or (i in {x[:-1] + y for x in a[:n]for y in a[:n]}) * 2)
