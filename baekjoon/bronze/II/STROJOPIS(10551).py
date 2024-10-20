A = input()
for l in ["1QAZ", "2WSX", "3EDC", "4RFV5TGB", "6YHN7UJM", "8IK,", "9OL.", "0P;/-['=]"]:
    print(sum(a in l for a in A))
