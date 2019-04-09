from time import time
from datetime import datetime
import math
class performance:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.start_time = time() 

    def __exit__(self,type, value, traceback):
        self.end_time = time()
        with open (self.file_name, 'a') as myfile:
            log = '{}. EXecution time: {} \n'.format(datetime.now(), self.end_time-self.start_time)
            myfile.write(log)


with performance('log_file.txt'):
    math.factorial(10000)



