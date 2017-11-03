""" 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.
What is the 10001st prime number?
"""

def is_prime(num):
    """ Return 'True' if 'num' is prime, 'False' if not.
    The primality test relay on the fact that all primes are of the form
    6k+1, 6k-1. This is checked at the last part of the test.
    """
    if num <= 1: return False # 0, 1 are composites
    if num <= 3: return True # 2, 3 are primes
    if num%2==0 or num%3==0: return False # multiples of 2, 3 are composites
    i = 5
    while i**2 <= num:
        if num%i==0 or num%(i+2)==0:
            return False
        i += 6
    return True

def main():
    """ We loop though all odd numbers, checking which is prime while keep a
    counter. The loop stops when we find the desired prime.
    """
    num, counter = 1, 1 # we skip 2, which is prime
    while counter < 10001:
        num += 2
        if is_prime(num): counter += 1
    print num

if __name__ == '__main__':
    main()