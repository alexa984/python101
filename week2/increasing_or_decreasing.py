def increasing_or_decreasing(seq):
    if all(seq[idx] < seq[idx+1] for idx in range (len(seq)-1)):
        return 'Up!' 
    elif all(seq[idx] > seq[idx+1] for idx in range (len(seq)-1)):
        return 'Down!' 
    else:
        return 'False'