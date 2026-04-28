# Palindrome
# Day 30

def isPalindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
