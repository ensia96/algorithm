n = int(input())
print(''.join(chr((ord(i)-65-(n := n+3)) % 26+65)for i in input()))
