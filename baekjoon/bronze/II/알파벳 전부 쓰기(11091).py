import string
A = string.ascii_lowercase
for i in [*open(0)][1:]:
    t = {*A}-{a for a in A if a in i.lower()}
    print(['pangram', 'missing '+''.join(sorted(t))][len(t) > 0])
