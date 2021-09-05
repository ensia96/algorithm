def merge_sort(l):
    if len(l) == 1:
        return l
    t = len(l)
    m = t//2
    a, b, c = merge_sort(l[:m]), merge_sort(l[m:]), []
    i = j = 0
    for _ in range(t):
        if j == t-m:
            c += [a[i]]
            i += 1
        elif i == m:
            c += [b[j]]
            j += 1
        elif a[i] <= b[j]:
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c


print(
    '\n'.join(map(str, merge_sort([int(input()) for _ in range(int(input()))]))))
