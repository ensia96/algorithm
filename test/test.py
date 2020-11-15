import time

data = input("여러가지 숫자로 이루어진 문자열을 입력해주세요.\n\n값 : ")

result = int(data[0])

start = time.time()

for i in range(1, len(data)):
    number = int(data[i])
    plus = result + number
    mult = result * number
    result = plus if mult <= plus else mult

print(f"수행 시간 : {time.time() - start} ms")

print(result)
