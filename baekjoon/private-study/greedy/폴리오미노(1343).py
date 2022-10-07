A = input()
print([A.replace('X'*4, 'A'*4).replace('XX', 'BB'), -1]
      [any(len(a) % 2 for a in A.split('.'))])
