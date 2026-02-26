_, *L = open(t := 0)
while L:
    _, A, B, *L = L
    t += 1
    j = 0
    print(
        f'Data Set {t}:\n{max(int(a) - B.split().count(str(j := j + 1))for a in A.split())}\n')
