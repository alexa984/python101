import sys
def find_char(str, ch):
    indices = []
    for i, c in enumerate(str):
        if c==ch:
            indices.append(i)
    return indices

def hangman(clue_word):
    guessing_word = '_'*len(clue_word)
    remaining_tries = 10

    while remaining_tries > 0 and guessing_word != clue_word:
        print('Guess a letter: ')
        letter = input()
        if clue_word.find(letter) == -1:
            remaining_tries-=1
        else:
            indices_of_letter = find_char(clue_word, letter)
            for idx in indices_of_letter:
                guessing_word = guessing_word[:idx] + letter + guessing_word[idx + 1:]
            print(guessing_word)
    if guessing_word == clue_word:
        print('Congratulations!')
    else:
        print('You lost!\n  ________\n|    |    |\n|  \ O /  |\n|    |    |\n|    |    |\n|   / \   |')


def main():
    print('Welcome to Hangman! Let\'s play!')
    print('-'*10)

    hangman(sys.argv[1])

if __name__ == '__main__':
    main()