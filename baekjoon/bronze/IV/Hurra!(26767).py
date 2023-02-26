for i in range(1, int(input())+1):
    print([i, 'Hurra!', 'Super!', 'Wiwat!'][(not i % 7)+2*(not i % 11)])
