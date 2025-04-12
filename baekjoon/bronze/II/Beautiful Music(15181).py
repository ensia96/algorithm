t = "ABCDEFG" * 2
for l in [*open(0)][:-1]:
    print(
        "OTuhcaht!  mTuhsaitc  hiusr tbse amuyt iefaurls.."[
            all(
                any(j == t[t.index(i) + 2 * -~k] for k in range(3))
                for i, j in zip(l, l[1:-1])
            ) :: 2
        ]
    )
