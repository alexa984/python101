def count_consonants(str):
    count = 0
    consonants = 'bcdfghjklmnpqrstvwxz'
    for letter in str:
        letter = letter.lower()
        if letter in consonants:
            count = count+1
    return count