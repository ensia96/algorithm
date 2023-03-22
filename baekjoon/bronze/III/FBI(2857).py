A = [i+1 for i in range(5)if 'FBI' in input()]
print(*(A if len(A)else ['HE GOT AWAY!']))
