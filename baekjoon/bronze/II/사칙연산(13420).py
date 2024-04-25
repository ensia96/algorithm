for l in [*open(0)][1:]:
    print(['wrong answer', 'correct'][eval(l.replace('=', '=='))])
