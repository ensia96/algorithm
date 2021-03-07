def solution(phone_book):
    '''
    input
        - phone_book : [전화번호] (1 <= [] <= 1000000, 1 <= i <= 20)
    output
        - answer     : 임의의 번호가 다른 번호의 접두어인 경우의 진리값
    result
        - 정확성 : 100/100
        - 효율성 : 100/100
    '''
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

# Fail

# 정답 출처 : https://velog.io/@vvakki_/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%B4%EC%8B%9C-%EC%A0%84%ED%99%94%EB%B2%88%ED%98%B8-%EB%AA%A9%EB%A1%9D

print(solution(["119", "97674223", "1195524421"])) # False
print(solution(["123", "456", "789"])) # True
print(solution(["12", "123", "1235", "567", "88"])) # False
