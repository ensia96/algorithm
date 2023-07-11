R = [i for i in range(100, 999)if i % 111]
for i in R:
    for j in R:
        i*(j % 100) == (i//10) * \
            j and i % 10 == j//100 and print(f'{i} / {j} = {i//10} / {j%100}')
