#__name__ = '__duhs.py__'
import os
import sys

def hbytes(num):
    for x in ['bytes','KB','MB','GB']:
        if num < 1000.0:
            return "%3.1f%s" % (num, x)
        num /= 1000.0
    return "%3.1f%s" % (num, 'TB')

def get_size(start_path):
    total_size = os.path.getsize(start_path)
    list_dir = os.listdir(start_path)

    for directory in list_dir:
        full_path = str(start_path + '/' + directory)
        if os.path.isdir(full_path):
            total_size+=get_size(full_path)
        else:
            total_size+=os.path.getsize(full_path)
    return total_size

def main():
    print(hbytes(get_size(sys.argv[1])), sys.argv[1])
    
if __name__ == '__main__':
    main()