##################################
# Test submit to github repository
##################################

# NOT FINAL PIECE OF WORK

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
    if any(char.isdigit() for char in seq1):
        print("Error, please enter sequence 1 in correct format with letters A, T, C or G")
    if any(char.isdigit() for char in seq2):
        print("Error, please enter sequence 2 in correct format with letters A, T, C or G")

    print("\nYou have entered \nSeq 1:", seq1, "\nSeq 2:", seq2)
    return seq1, seq2

#User input scoring schema



#def needleman_wunsch(seq1, seq2, match, mismatch, gap):



def main():
    #module code
    action()
    seq_input()


if __name__ == "__main__":
    main()
