# sum_numbers.py
import sys
import csv

def sum_numbers(filename):
    result=0
    f = open(filename, 'r+')
    numbers = str(f.readlines())
    numbers = numbers[2: len(numbers)-2]
    numbers = numbers.split(' ')
    for num in numbers:
        result += int(num)
    f.close()
    print(result)

def main():
    sum_numbers(sys.argv[1])

if __name__ == '__main__':
    main()