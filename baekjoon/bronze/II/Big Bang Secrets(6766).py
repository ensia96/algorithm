n = int(input())
t = 0
print(''.join(chr((ord(i)-65-3*(t := t+1)-n) % 26+65)for i in input()))
