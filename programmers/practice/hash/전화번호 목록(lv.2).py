def solution(phone_book):
    '''
    input
        - phone_book : [전화번호] (1 <= [] <= 1000000, 1 <= i <= 20)
    output
        - answer     : 임의의 번호가 다른 번호의 접두어인 경우의 진리값
    result
        - 정확성 : 54.2/100
        - 효율성 : 12.5/100
    '''
    table   = dict()
    index   = 0
    maximum = len(max(phone_book, key=len))

    for number in phone_book:
        table[number] = False

    while index < maximum:
        count = dict()

        for number in phone_book:
            if table[number]:
                continue
            digit = number[index]

            if digit not in count:
                count[digit] = 0
            count[digit] += 1

        if max(count.values()) == 1:
            return True

        for number in phone_book:
            if table[number]:
                continue

            if count[number[index]] >= 1:
                if len(number) - 1 == index:
                    return False
            else:
                table[number] = False

        index += 1

print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123", "456", "789"])) # True
print(solution(["12", "123", "1235", "567", "88"])) # False
