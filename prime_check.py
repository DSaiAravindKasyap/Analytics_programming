"""
This module implements the main functionality of Prime number checking.

Author: D Sai Aravind Kasyap
"""


class CheckPrime:
    def prime_check(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

