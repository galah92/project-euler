""" Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def main():
    """ Calculating the number, we'll sum up it's digits after converting it
    to a string an chopping it's digits.
    """
    N = 1000
    print reduce(lambda x, y: int(x)+int(y), str(2**N))

if __name__ == '__main__':
    main()