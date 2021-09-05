def quick_sort(a, s=0, e=0):
    e = [len(a), e][bool(e)]
    if e <= s+1:
        return a
    l, r = s+1, e-1
    while 1:
        while l <= r and a[l] <= a[s]:
            l += 1
        while l <= r and a[r] > a[s]:
            r -= 1
        if l > r:
            break
        a[l], a[r] = a[r], a[l]
    a[s], a[r] = a[r], a[s]
    quick_sort(a, s, r)
    quick_sort(a, r+1, e)
    return a


print(quick_sort([6, -8, 1, 12, 8, 3, 7, -7]))
