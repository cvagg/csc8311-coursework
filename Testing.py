##################################
# Test submit to github repository
##################################

# NOT FINAL PIECE OF WORK

import pandas as pd
import numpy as np
import re


def main():
    # module code
    print("**********\nWelcome to the sequence aligner "
          "\n**********"
          "\nSequences can be aligned globally using the "
          "Needleman and Wunch method or locally using the Smith Waterman method"
          "\n**********")

    # Sequence input
    s1, s2 = seq_input()

    # Sequence formatting for entering in matrix
    seq1 = split(s1)
    seq2 = split(s2)

    # global or local alignment:
    act = action()

    # change scoring schema?
    score = scoring(act)

    # changed schema
    if score:
        if act:
            n_w(seq1, seq2)
        else:
            s_w(seq1, seq2)

    # schema not changed
    else:
        match, mismatch, gap = score
        if act:
            n_w(seq1, seq2, match, mismatch, gap)
        else:
            s_w(seq1, seq2, match, mismatch, gap)



# User input alignment action
def action():
    """Retrieves wanted alignment, either global or local.
    Returns: act (action) True for global or False for local"""

    reply = str(input("\nPlease type which alignment you would like to run (G/L): ")).lower().strip()
    if reply[0] == "g":
        act = True
        return act
    if reply[0] == "l":
        act = False
        return act
    else:
        print("Error, please answer in correct format")
        return action()


# User Input of sequences
def seq_input():
    """Gets sequences for alignment from user"""
    print("Please input your sequences as nucleotides, can be either upper or lower case\n")
    b = True
    r = re.compile("(?i)^[ACTG]+$")
    while b:
        seq1 = input("Sequence 1: ")
        seq2 = input("Sequence 2: ")

        # check if sequence input matches format
        if r.match(seq1) and r.match(seq2):
            b = False
        else:
            print("Error, please enter sequences in desired format")
    # print("\nYou have entered \nSeq 1:", seq1, "\nSeq 2:", seq2)
    return seq1, seq2


def split(s):
    """returns list of char in input str. Source Geeks for Geeks.
    Could create a class where the string input is all formatted??"""
    return [char for char in s]

# User input scoring schema
def scoring(method):
    """prompts user to input scoring schema if they want to change default settings
    Input method either True (global) or False (local)"""

    # global
    if method:
        m = True
        while m:
            m = False
            print("You have selected global alignment, the default scoring schema is"
                  "\nmatch = 0"
                  "\nmismatch = 20"
                  "\ngap = 25")

            # y is act is true, n act is false
            reply = str(input("\nWould you like to change the scoring schema? (y/n)")).lower().strip()
            if reply[0] == "y":
                act = True
                #return act
            if reply[0] == "n":
                act = False
                #return act
            else:
                print("Error, please answer as y/n")
                m = True

        # user wants to change scoring schema
        if act:
            print("Please enter values of each penalty to update the scoring schema")
            match = input("\nmatch = ")
            mismatch = input("\nmismatch = ")
            gap = input("\ngap = ")
            return match, mismatch, gap

        else:
            return True


    # local
    else:
        m = True
        while m:
            m = False
            print("You have selected local alignment, the default scoring schema is"
                  "\nmatch = 5"
                  "\nmismatch = -3"
                  "\ngap = -5")

            # y is act is true, n act is false
            reply = str(input("\nWould you like to change the scoring schema? (y/n)")).lower().strip()
            if reply[0] == "y":
                act = True
                # return act
            if reply[0] == "n":
                act = False
                # return act
            else:
                print("Error, please answer as y/n")
                m = True

        # user wants to change scoring schema
        if act:
            print("Please enter values of each penalty to update the scoring schema")
            match = input("\nmatch = ")
            mismatch = input("\nmismatch = ")
            gap = input("\ngap = ")
            return match, mismatch, gap

        else:
            return True


    #return match, mismatch, gap

    # def prompt(method, match, mismatch, gap):
    #     m = True
    #     if method:
    #         a = "global"
    #     else:
    #         a = "local"
    #     while m:
    #         m = False
    #         print("You have selected {} alignment, the default scoring schema is \nmatch = {}"
    #               "\nmismatch = {}"
    #               "\ngap = {}".format(a, match, mismatch, gap))
    #
    #         # y is act is true, n act is false
    #         reply = str(input("\nWould you like to change the scoring schema? (y/n)")).lower().strip()
    #         if reply == "y":
    #             ans = True
    #         # return act
    #         elif reply == "n":
    #             ans = False
    #         # return act
    #         else:
    #             print("Error, please answer as y/n")
    #             m = True
    #
    #         # user wants to change scoring schema
    #     if ans:
    #         print("Please enter values of each penalty to update the scoring schema")
    #         match = int(input("\nmatch = "))
    #         mismatch = int(input("\nmismatch = "))
    #         gap = int(input("\ngap = "))
    #         return match, mismatch, gap
    #     else:
    #         return True
    #
    # # global
    # if method:
    #     match, mismatch, gap = prompt(method, 0, 20, 25)
    #
    # # local
    # else:
    #     match, mismatch, gap = prompt(method, 5, -3, -5)
    #
    # return match, mismatch, gap



# Needleman and Wunch function (global)
def n_w(seq1, seq2, match=0, mismatch=20, gap=25):
    """Returns optimal global alignment of 2 sequences from user input
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

                # min value is selected
                if (mis_score <= gap_side) and (mis_score <= gap_above):
                    smallest = mis_score
                elif (gap_side <= mis_score) and (gap_side <= gap_above):
                    smallest = gap_side
                else:
                    smallest = gap_above

                a[y, x] = smallest

    # implement array as pandas data frame
    nw_df = pd.DataFrame(data=a[1:], columns=a[0]).set_index(" ")
    nw_df.index.name = None

    # Global scoring matrix
    print("\nGlobal scoring matrix:", "\n", nw_df)

    # Optimal alignment(s) from matrix

        # start at (len(col), len(row)) work backwards

    return nw_df

# Smith Waterman algorithm
def s_w(seq1, seq2, match=5, mismatch=-3, gap=-5):
    """Returns optimal local alignment of two sequences from user input using the Smith Waterman method.
    Scoring schema is set as default but can be changed in calling of function in main module code."""

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
            if x == 1 or y == 1:
                a[y, x] = 0

            # match ?
            elif seq1[x] == seq2[y]:
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
                if (mis_score >= gap_side) and (mis_score >= gap_above):
                    largest = mis_score
                elif (gap_side >= mis_score) and (gap_side >= gap_above):
                    largest = gap_side
                else:
                    largest = gap_above

                a[y, x] = largest

    sw_df = pd.DataFrame(data=a[1:], columns=a[0]).set_index(" ")
    sw_df.index.name = None

    # Scoring matrix
    print("\nLocal scoring matrix:", "\n", sw_df)

    # Alignment
    def aligner(x,y,array,results=[]):
        results.append((x,y))
        vals = [array[x-1,y-1],array[x,y-1], array[x-1,y]]
        biggest = np.argmax(vals)

        if vals[biggest] == 0:
            return results

        if biggest == 0:
            return aligner(x-1,y-1,array,results)
        elif biggest == 1:
            return aligner(x, y - 1, array, results)
        else:
            return aligner(x - 1, y, array, results)

    algn = aligner(y,x,a)
    print("alignment positions:", algn)

    a_seq1 = []
    a_seq2 = []

    # make seq1 and seq2 the same length

    for i in algn:
        #print("i",i)
        y,x = i

        if seq1[x] == seq2[y]:  #match
            a_seq1.append(seq1[x])
            a_seq2.append(seq2[y])

        else:  #gap
            a_seq1.append(["-", seq1[x]])
            a_seq2.append(seq2[y])

    a = sw_df.max(axis=0)
    print(a_seq1, a_seq2)
    #print(a)
    return sw_df





if __name__ == "__main__":
    main()
