def solution(phone_book):
    '''
    input
        - phone_book : [전화번호] (1 <= [] <= 1000000, 1 <= i <= 20)
    output
        - answer     : 임의의 번호가 다른 번호의 접두어인 경우의 진리값
    '''
    phone_book.sort(key=len)

    table   = dict()
    index   = 0
    maximum = len(phone_book[-1])

    for i in range(maximum):
        table[i] = dict()

    while index < maximum:
        for number in phone_book:
            if len(number) - 1 < index:
                continue

            digit = number[index]
            cell  = table[index]

            if digit not in cell:
                cell[digit] = 0
            cell[digit] += 1

        index += 1

    return table

print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123", "456", "789"])) # True
print(solution(["12", "123", "1235", "567", "88"])) # False
