A = input()
print(['Inc', 'C'][A[:2] == 'io' and all(
    map(str.isnumeric, A[2:])) and len(A) > 2]+'orrect')
