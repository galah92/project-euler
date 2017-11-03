''' Largest palindrome product
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
'''

def problem004():
    ''' Each one of our two 3-digit numbers must lie between 100 and 999.
        But, it can be proven that the derised palindrome is divisble by 11.
        Thus, one of the numbers ('a' or 'b') is also divisible by 11.
        We can assume that 'a' is the one and implement the outer loop
        accordingly. We can also loop downwards and break if the number that is
        being checked is smaller then the largest palindrome currently stored.
    '''
    a, largest_palindrome = 990, 0 # 999 is largest 3-digit which div 11
    while a >= 100:
        b = 999
        while b >= 100:
            if str(a*b) == str(a*b)[::-1] and a*b > largest_palindrome:
                largest_palindrome = a*b
                break
            if a*b < largest_palindrome:
                break
            b -= 1
        a -= 11
    return largest_palindrome
