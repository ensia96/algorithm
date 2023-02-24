D = {'CU': 'see you', ':-)': 'I’m happy', ':-(': 'I’m unhappy', ';-)': 'wink', ':-P': 'stick out my tongue', '(~.~)': 'sleepy', 'TA': 'totally awesome',
     'CCC': 'Canadian Computing Competition', 'CUZ': 'because', 'TY': 'thank-you', 'YW': 'you’re welcome', 'TTYL': 'talk to you later'}
K = [*D.keys()]
while 1:
    A = input()
    print(A in K and D[A] or A)
    A == 'TTYL' and exit()
