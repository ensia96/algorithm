while (n := int(input())):
    p, x, y = min((2 * (i + n // i), i, n // i)
                  for i in range(1, n + 1)if 1 > n % i)
    print("Minimum perimeter is", p, "with dimensions", x, "x", y)
