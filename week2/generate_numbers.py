# generate_numbers.py
import sys
from random import randint


def generate_numbers(filename, numbers):
    f = open(filename, 'r+')
    f.truncate(0)   #to clear the screen
    for i in range(int(numbers)):
        if(i+1) < int(numbers):
            f.write(str(randint(1, 1000))+ ' ')
        else: 
            f.write(str(randint(1, 1000)))
    f.close()

def main():
    generate_numbers(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()