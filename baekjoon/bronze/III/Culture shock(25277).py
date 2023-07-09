_, *L = open(0).read().split()
print(sum(L.count(i)for i in ['he', 'she', 'him', 'her']))
