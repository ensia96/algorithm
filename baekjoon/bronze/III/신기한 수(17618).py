print(sum(not i % sum(map(int, str(i)))for i in range(1, int(input())+1)))
