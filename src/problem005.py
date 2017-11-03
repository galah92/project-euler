''' Smallest multiple
    2520 is the smallest number that can be divided by each of the numbers from
    1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
'''

from math import log


def primes_sieve(N):
    ''' Get a list of primes from 2 to N (including)
        Inspired by 'Sieve of Eratosthenes' method. 'sieve' is a list of
        booleans, when the value of each item tells if the number (which is
        represented by the position of the item) is prime.
        We loop through the list, and for each prime we enounter we change
        all it's multiples value to 'False'.
        N: upper limit for the generated list.
    '''
    sieve = [False, False] + [True]*(N-1) # 0 and 1 are not primes
    for num, is_prime in enumerate(sieve):
        if not is_prime:
            continue
        if num**2 > N:
            break # all non-primes beyond num**2 were already marked
        for not_a_prime in range(num**2, N+1, num):
            sieve[not_a_prime] = False # all products of num are not primes
    return [num for num, is_prime in enumerate(sieve) if is_prime]


def problem005():
    ''' The smallest number is the least common multiple (LCM) of the numbers
    from 1 to 20, which is composed of all primes that are comprising each
    of these numbers, when the exponents of each prime is set to the max of
    each prime.
    Thus, it can be proved that the max exponent get be calculated using
    logarithms, and specifically log(1..20)/log(primes-up-to-20).
    We can now find our answer easily
    '''
    result, N = 1, 20
    for prime in primes_sieve(N):
        result *= prime**int(log(N, prime))
    return result
