for l in [*open(0)][:-1]:
    print(
        l.strip()
        .replace("%", "%25")
        .replace(" ", "%20")
        .replace("!", "%21")
        .replace("$", "%24")
        .replace("(", "%28")
        .replace(")", "%29")
        .replace("*", "%2a")
    )
