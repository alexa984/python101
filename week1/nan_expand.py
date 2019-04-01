def nan_expand(n):
    result = ''
    if n > 0:
        while n>0:
            n=n-1
            result+="Not a "
        result+="Nan"
    return result