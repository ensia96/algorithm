def checktree(x):
    n = len(x)
    if n == 1:
        return 1
    r = n//2
    if x[r] == '1':
        return checktree(x[:r])*checktree(x[r+1:])
    else:
        return not (int(x[:r]) or int(x[r+1:]))


def solution(numbers):
    A = []
    for n in numbers:
        b = bin(n)[2:]
        x = len(b)
        i, j = 1, 2
        while i < x:
            i += j
            j *= 2
        b = '0'*(i-x)+b
        A += +checktree(b),
    return A


print(solution([7, 5]))
print(solution([63, 111, 95]))
print(solution([10**15, 10**15-4, 562949953421311]))
