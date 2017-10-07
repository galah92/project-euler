''' Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sequence_sum(diff, limit):
    ''' Calculate and return the sum of a sequence which looks like
        diff, diff * 2, diff * 3, ..., limit
    '''
    return diff * (limit // diff) * (limit // diff + 1) // 2


def problem001():
    ''' Summing the sequences and substracting the numbers that where
        counted twice
    '''
    return sequence_sum(3, 999) + sequence_sum(5, 999) - sequence_sum(15, 999)
