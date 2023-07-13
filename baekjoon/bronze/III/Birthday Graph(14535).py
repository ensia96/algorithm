x = y = 1
while x:
    x = int(input()) or exit()
    L = [[*map(int, input().split())][1]for _ in ' '*x]
    print(f'Case #{y}:')
    for i in range(12):
        print('JanFebMarAprMayJunJulAugSepOctNovDec'[
              i*3:i*3+3]+':'+'*'*L.count(i+1))
