print(f"{(A:=int(input()))}:")
for i in range(2, A):
    A % (i+i-1) in [0, i] and print(i, i-1, sep=',')
    A % i == 0 and print(i, i, sep=',')
