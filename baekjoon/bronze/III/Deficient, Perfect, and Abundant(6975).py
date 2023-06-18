for l in [*open(0)][1:]:
    n = int(l)
    x = sum(i for i in range(1, n)if not n % i)
    print(n, 'is', ['a perfect', 'a deficient', 'an abundant']
          [(x < n)+2*(n < x)], 'number.')
