def char_histogram(string):
    out = {}
    for c in string:
        out[c] = out.get(c, 0) + 1
    return out