import sys
sys.path.insert(0, '/home/alexandra/Documents/python101/week1')
from palindrome import palindrome
def get_largest_palindrome(n):
    for i in reversed(range(n)):
        if palindrome(i):
            return i

print(get_largest_palindrome(754649))
