for l in [*open(0)][1:]:
    print(f'{l}{+(len(l)-1<sum(map(l.count,"aeiou"))*2)}')
