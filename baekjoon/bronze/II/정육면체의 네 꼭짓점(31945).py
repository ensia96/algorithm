for l in [*open(0)][1:]:
    print(
        "YNEOS"["".join(sorted(l.split())) not in "0123 0145 0246 1357 2367 4567" :: 2]
    )
