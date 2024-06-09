*A, = map(int, [*open(0)][1].split())
for a in A:
    y = sum({i for i in range(2, a)if a % i < 1})+1
    print([['Perfect', 'Abundant'][y > a], 'Deficient'][y < a])
