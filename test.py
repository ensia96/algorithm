def absoluteValuesSumMinimization(a):
    alist = [sum(map(lambda x: abs(x - num), a)) for num in a]
    return a[alist.index(min(alist))]


print(absoluteValuesSumMinimization([2, 4, 7]))
# => should return 4
