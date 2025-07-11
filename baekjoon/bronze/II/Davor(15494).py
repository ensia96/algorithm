n = int(input())
print(*[[i, x//1092]for i in range(101)[::-1]
      if (x := n-364*i) > 0 and not x % 1092][0], sep='\n')
