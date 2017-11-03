""" Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which, a^2 + b^2 = c^2. For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

def main():
    """ From Euclid's formula we know that:
    (a = m^2 - n^2), (b = 2*m*n), (c = m^2 + n^2), (m > n)
    We also know that a + b + c = N(=1000), thus we can derive:
    (m^2 - n^2) + (2*m*n) + (m^2 + n^2) = N, or: (m * (m+n) = N/2)
    Since m > n and m > 0, we can evaluate lower and upper bounds for m:
    sqrt(N/2) > m > sqrt(N)/2.
    From here we can loop over the possible values of m and solve.
    """
    N = 1000
    for m in xrange(int(sqrt(N)/2), int(sqrt(N/2))):
        n = N / (2.0*m) - m # n type is 'float'
        if m > n > 0 and n.is_integer():
            a, b, c = m**2 - int(n)**2, 2*m*int(n), m**2 + int(n)**2
            print a * b * c
            break

if __name__ == '__main__':
    main()