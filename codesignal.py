def ExistPlus_Non1(input_d, k):
    if k in input_d.keys():
        input_d[k] += 1
    else:
        input_d[k] = 1


def DestructNum(n):
    if n >= 2:
        i = 2
        r = {}
        while n >= 2:
            if n % i == 0:
                ExistPlus_Non1(r, i)
                n = n // i
            else:
                i += 1
        return r
    else:
        return {1: 1}


def DictToList(input_d):
    r = []
    for k in input_d.keys():
        r += [k for i in range(0, input_d[k])]
    return r


def IsPrimeAndOver10(n):
    c = 0
    if n < 10:
        return False
    for i in range(2, n):
        if n % i == 0:
            c += 1
    return False if c >= 1 else True


def digitsProduct(product):
    if product == 0:
        return 10
    n_dict = DestructNum(product)
    if any([IsPrimeAndOver10(k) for k in n_dict.keys()]):
        return -1
    else:
        while True:
            if 3 in n_dict.keys() and n_dict[3] >= 2:
                n_dict[3] -= 2
                ExistPlus_Non1(n_dict, 9)
            else:
                if 2 in n_dict.keys() and n_dict[2] >= 3:
                    n_dict[2] -= 3
                    ExistPlus_Non1(n_dict, 8)
                else:
                    if (
                        2 in n_dict.keys()
                        and n_dict[2] >= 1
                        and 3 in n_dict.keys()
                        and n_dict[3] >= 1
                    ):
                        n_dict[2] -= 1
                        n_dict[3] -= 1
                        ExistPlus_Non1(n_dict, 6)
                    else:
                        if 2 in n_dict.keys() and n_dict[2] >= 2:
                            n_dict[2] -= 2
                            ExistPlus_Non1(n_dict, 4)
                        else:
                            break
    return int("".join([str(d) for d in sorted(DictToList(n_dict))]))


# https://frhyme.github.io/algorithm/Algorithm-digitsProduct/
# 1 ~ 9 사이의 수로 반복적으로 나누게 하는 반복문에 대한 종결값 설정, 나누기를 1로 시작하지 않는 반복문의 조건설정을 못해서 구글링함.

# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


def digitsProduct(p):
    if p == 0:
        return 10
    elif p == 1:
        return 1

    n = []

    while 1 < p:
        for d in range(9, 1, -1):
            if p % d == 0:
                p /= d
                n.append(d)
                break
        else:
            return -1

    return int("".join(map(str, sorted(n))))


# ================================================#
#                 question v                     #
# ================================================#

# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

# Example

# For product = 12, the output should be
# digitsProduct(product) = 26;
# For product = 19, the output should be
# digitsProduct(product) = -1.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer product

# Guaranteed constraints:
# 0 ≤ product ≤ 600.

# [output] integer
