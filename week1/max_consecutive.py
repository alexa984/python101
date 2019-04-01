def max_consecutive(items):
    max=1;
    curr=1
    prev = items[0]
    for i in items:
        if i==prev:
            curr=curr+1
        else:
            if curr>max:
                max = curr
            curr=1
        prev = i
    return max