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

# 신입 공채 당시에 제출했던 코드
#
# from math import sqrt
#
#
# def is_prime(n):
#     for i in range(2, int(sqrt(n))+1):
#         if n % i == 0:
#             return False
#     return True
#
#
# def solution(n, k):
#     if k != 10:
#         converted = ''
#         while n:
#             n, mod = divmod(n, k)
#             converted += str(mod)
#             converted = converted[::-1]
#     else:
#         converted = str(n)
#
#     candidates = [*map(int, [*filter(None, converted.split('0'))])]
#     scope = max(candidates)
#
#     need_refine = {a: candidates.count(a)
#                    for a in set(candidates) if is_prime(a) and a > 1}
#
#     return sum(need_refine[num] for num in need_refine)
