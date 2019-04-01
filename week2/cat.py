import sys

def cat(argument):
    f = open(argument, 'r')
    my_lines = f.readlines()
    for line in my_lines:
        print(line.strip('\n'))
    f.close()

def main():
    cat(sys.argv[1])

if __name__ == '__main__':
    main()
