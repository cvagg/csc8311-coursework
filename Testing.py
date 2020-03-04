##################################
# Test submit to github repository
##################################

# NOT FINAL PIECE OF WORK

import pandas as pd
import numpy as np


def main():
    # module code
    #action()
    s1, s2 = seq_input()
    seq1 = split(s1)
    seq2 = split(s2)
    n_w(seq1,seq2)


# User input alignment action
def action():
    """Retrieves wanted alignment, either global or local.
    Returns: act (action) either G for global or L for local"""
    b = True
    while b:
        b = False
        act = input("\nPlease type which alignment you would like to run "
                    "\n G for global alignment or L for local alignment: ")
        if act is not "G" and act is not "L":
            print("Error, please answer in correct format")
            b = True
    return act


# User Input of sequences
def seq_input():
    """Gets sequences for alignment from user"""
    seq1 = input("Please enter sequence 1: ")
    seq2 = input("Please enter sequence 2: ")

    ## Could expand this with extra precautions
    ## add a regex to see if the str actually contains bases and only bases- no other chars
    ## Do they have to be the same length?
    # if any(char.isdigit() for char in seq1):
    #    print("Error, please enter sequence 1 in correct format with letters A, T, C or G")
    # if any(char.isdigit() for char in seq2):
    #    print("Error, please enter sequence 2 in correct format with letters A, T, C or G")

    # print("\nYou have entered \nSeq 1:", seq1, "\nSeq 2:", seq2)
    return seq1, seq2


def split(s):
    """returns list of char in input str. Source Geeks for Geeks.
    Could create a class where the string input is all formatted??"""
    return [char for char in s]

# User input scoring schema
###NEEDS WORK####

# Needleman and Wunch function
def n_w(seq1, seq2, match=0, mismatch=20, gap=25):
    """Returns optimal global alignment of sequences 1 and 2 from user input
    using the Needleman and Wunch dynamic programming method. Scoring schema is set as default
    but can be changed in calling of function in main() module code"""

    # add Gap penalty col and row for each sequence
    seq1.insert(0, " ")
    seq1.insert(1, "0")  # 0 means gap penalty
    seq2.insert(0, " ")
    seq2.insert(1, "0")

    # create empty array (matrix)
    a = np.full((len(seq2), len(seq1)), " ", dtype="object")

    # change headers
    a[0, :] = seq1  # x-axis header (seq1)
    a[:, 0] = seq2  # y-axis header (seq2)

    # set gap scores to zero
    gap_x = 0
    gap_y = 0

    for x in range(1, len(seq1)):
        for y in range(1, len(seq2)):

            # initial gap penalties
            if x == 1 and y == 1:
                gap_x = 0
                a[y, x] = gap_x
            elif y == 1:
                gap_y = gap_y + gap
                a[y, x] = gap_y
            elif x == 1:
                gap_x = gap_x + gap
                a[y, x] = gap_x

            # match ?
            elif seq1[x] == seq2[y]:
                # a[y,x] = "match"
                a[y, x] = a[y - 1, x - 1] + match

            # mismatch/gap
            else:
                # a[y,x] = "mismatch"

                # mismatch (diagonal)
                mis_score = a[y - 1, x - 1] + mismatch

                # gap score from side
                gap_side = a[y, x - 1] + gap

                # gap score from above
                gap_above = a[y - 1, x] + gap

                # max value is selected
                if (mis_score <= gap_side) and (mis_score <= gap_above):
                    smallest = mis_score
                elif (gap_side <= mis_score) and (gap_side <= gap_above):
                    smallest = gap_side
                else:
                    smallest = gap_above

                a[y, x] = smallest

    # implement array as pandas data frame
    nw_df = pd.DataFrame(data=a)
    print("Scoring matrix:", "\n", nw_df)
    return nw_df


if __name__ == "__main__":
    main()
