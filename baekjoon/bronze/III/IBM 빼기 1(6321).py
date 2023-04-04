print('\n\n'.join([f'String #{i+1}\n'+''.join([chr(65+(ord(i)+1) %
      65 % 26)for i in input()])for i in range(int(input()))]))
