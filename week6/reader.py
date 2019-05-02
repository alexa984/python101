import os
import keyboard

def reader(path):
    directories = os.listdir(path)
    directories.sort()
    for d in directories:

        with open(path+d, 'r') as read_file:
            lines_list = []
            for line in read_file:
                lines_list.append(line)

            start=0
            for idx,line in enumerate(lines_list):
                if line.startswith('# Chapter '):
                    curr_chapter=''
                    for line in lines_list[start:idx]:
                        curr_chapter+= line
                        
                    keyboard.wait(chr(32))
                    yield curr_chapter
                    start = idx


my_reader = reader('/home/alexandra/Documents/python101/week6/book/')
for chapter in my_reader:
    print(chapter)
    print('=======')



