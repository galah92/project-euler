""" Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def chain_length(n, chains):
    """ Return the chain length of a number n.
        If the chain length of n isn't stored yet, then calculate it according
        to the collatz sequence rules recursively and store it for future
        reference. Also store all the chain lengths for numbers that are found
        during the recursive iterations.
    """
    if not n in chains:
        chains[n] = 1 + chain_length(n/2 if n%2==0 else n*3+1, chains)
    return chains[n]

def main():
    """ Iterating over the numbers between 0-N, we'll find their chain length
    using the memoization principle. Each new chain length will be stored
    in a dictionary and will be retrived when relevant. Thus we don't need to
    calculate the chain length from the beginning for every new number.
    """
    N, chains = 1000000, {}
    largest_chain = (1, 1) # first is num, second is chain length
    chains[1] = 1
    for num in xrange(2, N):
        chain = chain_length(num, chains)
        if chain > largest_chain[1]:
            largest_chain = (num, chain)
    print largest_chain

if __name__ == '__main__':
    main()