A = []
for i in range(5):
    x = input()
    if (x.find('FBI') > 0)*len(x) == sum(map(lambda f: sum(map(f, x)),
                                             [str.isupper, str.isdigit, lambda i:i == '-'])): A += i+1,
print(*(A if len(A)else ['HE GOT AWAY!']))
