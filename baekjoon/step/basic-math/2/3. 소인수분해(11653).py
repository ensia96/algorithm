n = int(input())

while n != 1:
    i = 2
    while True:
        if not n % i:
            print(i)
            n //= i
            break
        i += 1
