def reverse_string(string):
    result = ''
    n = len(string)
    for i in range(n):
        result += string[n - i - 1]
    return result

def palindrome(obj):
    return str(obj) == reverse_string(str(obj))