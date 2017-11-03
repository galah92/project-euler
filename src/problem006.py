""" Sum square difference
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is:
( 1 + 2 + ... + 10 )^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

def main():
    """ The square of sum consists of sum of numbers from 1 to N (100),
    which can be calculated by the formula: Sn = n*(n+1)/2.
    The sum of squares can also bu calculated by a formula:
    Sn = n*(n+1)(2*n+1)/6. Combining these formulas we can solve easily.
    """
    N = 100
    print (((N * (N+1)) / 2) ** 2) - (N * (N+1) * (2*N+1) / 6)

if __name__ == '__main__':
    main()