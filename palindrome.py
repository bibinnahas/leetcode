import re

def is_palindrome(s):
    cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)
    return cleaned_s == cleaned_s[::-1]

if __name__ == '__main__':
    print(is_palindrome("racecar"))
