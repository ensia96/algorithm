while (n := int(input())):
    i = max(i * (1 > n % i)for i in range(1, int(n**.5) + 1))
    print('Minimum perimeter is', 2 * (i // n + n),
          'with dimensions', n, 'x', i // n)
