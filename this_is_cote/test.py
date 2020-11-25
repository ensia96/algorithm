n, people = int(input("전체 모험가의 수 : ")), sorted(map(int, input("모험가들의 공포도 : ").split()))

count, result = 0, 0

for person in people:
    count += 1
    if person <= count:
        result += 1
        count = 0

print(result)

# import time
# start = time.time()
# print(f"수행 시간 : {time.time() - start} ms")

# ================================================#
#     ^ right answer   ||     wrong answer v      #
# ================================================#

n = int(input("전체 모험가의 수 : "))

people = sorted(map(int, input("모험가들의 공포도 : ").split()), reverse=True)

i, result = 0, 0

while True:
    if i >= n:
        break
    i += people[i]
    result += 1

print(result)
