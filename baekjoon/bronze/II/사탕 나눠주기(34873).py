from collections import Counter
n, A = open(0)
print('YNeos'[max(Counter(A.split()).values()) > 2::2])
