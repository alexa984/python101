def count_vowels(str):
    count = 0
    for letter in str:
        letter = letter.lower()
        if letter in {'a', 'e', 'o', 'u', 'i', 'y'}:
            count = count+1
    return count