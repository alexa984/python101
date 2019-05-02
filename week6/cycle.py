def cycle(iterable):
    index = 0
    while True:
        if index == len(iterable):
            index = 0
        yield iterable[index]
        index+=1