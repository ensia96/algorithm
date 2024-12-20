t = 0
while (n := int(input())) != 0:
    print(
        f"Case #{(t:=t+1)}:{sum([sum(T:=[*map(int,input().split())]),T[0]+(1<len(T)and T[-1])][len(T)<n]for _ in' '*n)}"
    )
