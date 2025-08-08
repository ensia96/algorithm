s, e = map(int, input().split())
for i in map(str, range(s, e+1)):
    print([i, 'Palindrome!'][i == i[::-1]])
