check = [False, False] + [True] * 10000

for i in range(2, 101):
    if check[i] == True:
        for j in range(i + i, 10001, i):
            check[j] = False

for _ in range(int(input())):
    A = int(input()) // 2
    B = A
    for _ in range(10000):
        if check[A] and check[B]:
            print(A, B)
            break
        A -= 1
        B += 1

# 틀린 부분을 모르겠어서 참고한 글 : https://yoonsang-it.tistory.com/31
