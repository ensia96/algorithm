n = int(input())


def factorial(k):
    fact = 1
    for i in range(1, k+1):
        fact *= i
    return fact


def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))


print(nCr(n, 5))
