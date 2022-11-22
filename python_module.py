"""
This module implements the main functionality of Prime number checking and palindrome checking.

Author: D Sai Aravind Kasyap
"""
def prime_check(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True
    
def palindrome_check(n):
    str_in = n.casefold()
    rev = reversed(str_in)
    if list(str_in) == list(rev):
        return "Palindrome!"
    else:
        return "Not palindrome!"
