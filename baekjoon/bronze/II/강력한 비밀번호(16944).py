n = int(input())
A = input()
t = (
    4
    - any(map(str.isupper, A))
    - any(map(str.islower, A))
    - any(map(str.isdigit, A))
    - any(map(lambda x: x in "!@#$%^&*()-+", A))
)
print([t + 6 - n, t][n + t > 5])
