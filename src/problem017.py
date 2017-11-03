""" Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of 'and' when writing out numbers is in compliance with
British usage.
"""

def main():
    """ Iterating over the desired numbers, we'll add their sum of letters
    accordingly, using two lists of the base numbers and their words length.
    """
    N, total = 1000, 0
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    for num in xrange(1, N):
        c = num % 10 # ones digit
        b = (num % 100 - c) / 10 # tens digit
        a = (num % 1000 - b * 10 - c) / 100 # hundreds digit
        if a != 0:
            total += ones[a] + 7 # ones[a] 'hundred'
            if b != 0 or c != 0: total += 3 # 'and'
        total += ones[b*10 + c] if b==0 or b==1 else tens[b] + ones[c]
    print total + 11 # 'one thousand'

if __name__ == '__main__':
    main()