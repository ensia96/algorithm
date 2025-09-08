A, B = open(0)
print('Is', ['not ', ''][all(a == ' ' or B.count(a) == A.count(a)
      for a in A)] + 'an anagram.')
