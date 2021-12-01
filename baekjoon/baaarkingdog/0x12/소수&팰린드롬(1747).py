m = 10**6+3001
p = [0, 0]+[1]*(m-1)
for i in range(2, m+1):
    if p[i]:
        p[i+i::i] = [0]*(m//i-1)
for i in range(int(input()), m+1):
    if p[i] and (str(i) == str(i)[::-1]):
        exit(print(i))
