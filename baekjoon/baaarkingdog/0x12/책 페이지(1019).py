N = n = int(input())
A, c = [0]*10, 1
while n:
    n, r = divmod(n, 10)
    for i in range(10):
        A[i] += (n+(1 <= i <= r))*c-(c-(N % c)-1)*(i == r)
    c *= 10
print(*A)

# 풀이 참고 : https://latter2005.tistory.com/54
