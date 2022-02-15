def solution(n, k):
    a, A = '', 0
    while n:
        a = str(n % k)+a
        n //= k
    for i in [int(i)for i in a.split('0')if i]:
        if i < 2:
            continue
        e = int(i**.5)+1
        for j in range(2, e):
            if not i % j:
                break
        else:
            A += 1
    return A
