""" Names scores
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.
For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
would obtain a score of 938 * 53 = 49714.
What is the total of all the names scores in the file?
"""

def main():
    """ Using a bunch of 'pythonic' tools, we'll calculate the alphabetical
    value of each name using the built-in 'ord' function.
    From there and on we'll evaluate a score for each name and sum it all up.
    """
    names = sorted(eval('['+open('022_names.txt', 'rU').read()+']'))
    alpha_value = lambda name: sum(ord(letter)-64 for letter in name)
    print sum([alpha_value(name)*(i+1) for i, name in enumerate(names)])

if __name__ == '__main__':
    main()