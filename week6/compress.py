def compress(iterable, mask):
    for i in range (len(mask)):
         if mask[i]:
            yield iterable[i]
            