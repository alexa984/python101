
#task11 todo
#def prime_factorization(n):

#todo:word count
#todo: redo the following functions:

# def numbers_to_message(pressed_sequence):
#     seq_as_str = ''.join(map(str, pressed_sequence))
#     result = []
#     decode_dict = {
#     '2': 'a',
#     '22': 'b',
#     '222': 'c',
#     '3': 'd',
#     '33': 'e',
#     '333': 'f',
#     '4': 'g',
#     '44': 'h',
#     '444': 'i',
#     '5': 'j',
#     '55': 'k',
#     '555': 'l',
#     '6': 'm',
#     '66': 'n',
#     '666': 'o',
#     '7': 'p',
#     '77': 'q',
#     '777': 'r',
#     '7777': 's',
#     '8': 't',
#     '88': 'u',
#     '888': 'v',
#     '9': 'w',
#     '99': 'x',
#     '999': 'y',
#     '9999': 'z',
#     '0': ' '
#     }
#     for i in range(len(seq_as_str)):
#         if seq_as_str == '-':
#             seq_as_str[i]='0'

#     nums = [item[0] for item in re.findall(r"((.)\2*)", seq_as_str)]
#     for num in nums:
#         result.append(decode_dict[num])

#     return result

# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))


def message_to_numbers(message: str):
    symbols = {
    'a' : '2',
    'b' : '22',
    'c' : '222',
    'd' : '3',
    'e' : '33',
    'f' : '333',
    'g' : '4'
     ... 'z': '9999'
    }
    keystrokes = []
    for letter in message:
        if letter.isupper():
            keystrokes.append(1)
        if letter ==' ':
            keystrokes.append(int(SPACE_KEY))
# print(goldbach(4))
# print(goldbach(100))
