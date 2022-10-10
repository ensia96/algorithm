c = 0
for i in input():
    if c < 4:
        c += i == 'UCPC'[c]
print('I', ['love', 'hate'][c < 4], 'UCPC')
