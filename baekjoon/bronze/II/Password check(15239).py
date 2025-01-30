for l in [*open(0)][2::2]:
    print(
        (
            1
            ^ (len(l) > 12)
            * any(i.islower() for i in l)
            * any(i.isupper() for i in l)
            * any(i.isdigit() for i in l)
            * any(i in "+_)(*&^%$#@!./,;{}" for i in l)
        )
        * "in"
        + "valid"
    )
