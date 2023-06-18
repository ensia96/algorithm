for l in [*open(0)][1:]:
    n = int(l)
    x = sum(i+n//i for i in range(1, n//2)if not n % i)-n
    print(n, 'is', ['a perfect', 'a deficient', 'an abundant']
          [(x < n)+2*(n < x)], 'number.')
