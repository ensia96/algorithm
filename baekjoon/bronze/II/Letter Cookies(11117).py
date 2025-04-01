for _ in " " * int(input()):
    t = input()
    for _ in " " * int(input()):
        l = input()
        print("YNEOS"[any(t.count(i) < l.count(i) for i in l) :: 2])
