# csc8311: Coursework README file

## About
This program is designed to take in two DNA sequences in string format and return a scoring matrix of their alignment. The scoring schema for this matrix can either be left as a default or can be changed when prompted in the terminal. The scoring matrix is computed using dynamic programming of exact alginment methods for both global and local alignments. The user can choose which alginment they would like to perform within the terminal. The global alignments are conducted using the [Needleman and Wunch method](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm) and local alignments are conducted using the [Smith Waterman method](https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm).

## Requirements
This program works best within an IDE e.g. pycharm. However, if run inside a terminal such as linux the input from prompts must be entered in string format " ".

## Further Work
If I had more time I would implement a file read option where users could load a fasta file containing the two sequences instead of inputting them in the command line. I also wanted to display the optimal alignment that the scoring matrix computed but did not have enough time. Please see the opt_align.txt file in this repository with some pseudocode on how I would implement this if I had more time to work on it.

e.g.

**For the sequences atg and ggaatg:**

The Global Scoring Matrix:

         0    a   t   g
    0    0   25  50  75
    g   25   20  45  50
    g   50   45  40  45
    a   75   50  65  60
    t  100   75  50  75
    g  125  100  75  50

The aligned sequences output:

    seq1: ggaatg
    seq2: ___atg
      __a_tg
    2 optimal alignments found
