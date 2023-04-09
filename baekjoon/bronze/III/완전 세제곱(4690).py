R = range
for i in R(100):
    for j in R(2, i):
        for k in R(j, i):
            for l in R(k, i):
                i**3 == j**3+k**3 + \
                    l**3 and print(f'Cube = {i}, Tripple = ({j},{k},{l})')
