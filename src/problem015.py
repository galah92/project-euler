""" Lattice paths
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

from math import factorial

def main():
    N = 20
    print factorial(N * 2) / factorial(N)**2

if __name__ == '__main__':
    main()