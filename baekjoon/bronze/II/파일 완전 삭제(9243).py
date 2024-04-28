n, a, b = open(0).read().split()
print('Deletion', ['failed', 'succeeded']
      [all([a[i] != b[i], a[i] == b[i]]for i in range(len(a)))])
