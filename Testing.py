##################################
# Test submit to github repository
##################################

# NOT FINAL PIECE OF WORK

import pandas as pd


# User input alignment action
def action():
    """Retrieves wanted alignment, either global or local.
    Returns: act (action) either G for global or L for local"""
    b = True
    while b:
        b = False
        act = input("\nPlease type which action you would like to run "
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

def split(str):
    """returns list of char in input str. Source Geeks for Geeks.
    Could create a class where the string input is all formatted??"""
    return [char for char in str]


# User input scoring schema
###NEEDS WORK####

# Needleman and Wunch function
def n_w(seq1, seq2, match=0, mismatch=20, gap=25):
    """Returns optimal global alignment of sequences 1 and 2 from user input
    using the Needleman and Wunch dynamic programming method. Scoring schema is set as default
    but can be changed in calling of function in main() module code"""

    # create cols for empty matrix
    s_1 = split(seq1)
    s_2 = split(seq2)

    s_1.insert(0, "gap")
    s_2.insert(0, "gap")

    df = pd.DataFrame(columns=s_1, index=s_2)
    #print(df) #to print empty matrix

    ### Create dictionary to input into matrix one col at a time? ###

    # Gap key
    g_items = []

    # loop through split sequence list to get gap penalty for first col
    score = 0
    for i in range(len(s_2)):
        if i == 0:
            score = 0
        else:
            score = score + gap
        g_items.append(score)

    # print(g_items) #[0, 25, 50, 75]

    # other cols, match, mismatch or gap?
    score = 0
    test_items = []
    for n in range(len(seq1)):
        if seq1[n] ==
    # print(n)
    # if seq2[n] == seq1[n]: #match
    #    score = g_items[n-1] + gap
    #    test_items.append(score)

    # print("test", test_items)

    # for dictionary of other cols after gap
    mismatch = 20
    match = 0
    is_equal = {True: match, False: mismatch}

    # for x in range(2,len(seq1) + 2):
    #    for y in range(2,len(seq2) + 2)

    print(range(2, len(seq1) + 2))
    print(seq1)


# Module code
def main():
    # module code
    action()
    seq_input()


if __name__ == "__main__":
    main()
