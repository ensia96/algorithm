for i in range(int(input())):
    a, b = map(eval, input().split('='))
    print(f"Case {i+1}:", 'YNEOS'[a != b::2])
