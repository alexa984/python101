import sys

def cat2(arguments):
    files = arguments[1:]
    for file in files:
        f = open(file, 'r')
        my_lines = f.readlines()
        for line in my_lines:
            print(line.strip('\n'))
        print()
        f.close()

def main():
    cat2(sys.argv)

if __name__ == '__main__':
    main()
