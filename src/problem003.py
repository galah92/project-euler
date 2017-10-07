''' Largest prime factor
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
'''


def problem003():
    ''' Basic trial division test
    '''
    factor, num = 1, 600851475143
    while num % 2 == 0:
        num /= 2
    while num > 1:
        factor += 2
        while num % factor == 0:
            num /= factor
    return factor
