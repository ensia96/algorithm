def solution(phone_book):
    '''
    input
        - phone_book : [전화번호] (1 <= [] <= 1000000, 1 <= i <= 20)
    output
        - answer     : 임의의 번호가 다른 번호의 접두어인 경우의 진리값
    '''
    table = dict()
    index = 0

    phone_book.sort(key=len)

    for i in range(len(phone_book[-1])):
        table[i] = dict()

    return table

print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123", "456", "789"])) # True
print(solution(["12", "123", "1235", "567", "88"])) # False
