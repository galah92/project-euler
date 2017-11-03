""" Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

def main():
    """ The solution is inspired by 'Sieve of Eratosthenes' method.
    'sieve' is a list of booleans, when the value of each item tells if the
    number (which is represented by the position of the item) is prime.
    We loop through the list, and for each prime we encounter we change all
    it's multiples calue to 'False'. We sum our 'sieve' in the end.
    """
    N , sum_of_primes = 1999999, 0 # N is upper limit for the list
    sieve = [False, False] + [True]*(N-1) # 0 and 1 are not primes
    for num, is_prime in enumerate(sieve):
        if not is_prime: continue
        if num**2 > N: break # all non-primes beyond num**2 were already marked
        for not_a_prime in range(num**2, N+1, num):
            sieve[not_a_prime] = False # all products of num are not primes
    print sum(num for num, is_prime in enumerate(sieve) if is_prime)

if __name__ == '__main__':
    main()