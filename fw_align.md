# Further Work: Alignment functions

## For global methods
1. Alignment starts at (n,m) where n and m are the lengths of the two sequences to align i.e. (7,4)
2. The position of that is noted in terms of the two sequences i.e. (g,g)
3. The diagonal positon is taken (n-1,m-1) and noted i.e. (t,t)
4. This is repeated until the score of the diagonal position is zero
5. These positions are scored
6. If they are the same the two are aligned, if they are different a "_" is inserted

Example:
Sequences atg and ggaatg
    df =
         0    a    t   g
    0    0   25   50  75
    g   25   20   45  50
    g   50   45   40  45
    a   75   50   65  60
    a  100   75   70  85
    t  125  100   75  90
    g  150  125  100  75


## For local methods
1. Alignment starts at position with the largest score
2. Working backwards, the largest scoring position is taken next
3. This continues until the score is zero
4. Like in global, the positions with that match are aligned and those that aren't have "_" inserted

Example:
Using the same sequences
    df =
       0   a   t   g
    0  0   0   0   0
    g  0  -3  -3   5
    g  0  -3  -6   2
    a  0   5   0  -3
    a  0   5   2  -3
    t  0   0  10   5
    g  0  -3   5  15
    
Idea of function to get positions of aligned sequence:

        def aligner(x, y, array, results=[]):
        results.append((x, y))
        vals = [array[x - 1, y - 1], array[x, y - 1], array[x - 1, y]]
        biggest = np.argmax(vals)

        if vals[biggest] == 0:
            return results

        if biggest == 0:
            return aligner(x - 1, y - 1, array, results)
        elif biggest == 1:
            return aligner(x, y - 1, array, results)
        else:
            return aligner(x - 1, y, array, results)

    algn = aligner(y, x, a)
    print("alignment positions:", algn)

    a_seq1 = []
    a_seq2 = []

    # make seq1 and seq2 the same length

    for i in algn:
        # print("i",i)
        y, x = i

        if seq1[x] == seq2[y]:  # match
            a_seq1.append(seq1[x])
            a_seq2.append(seq2[y])

        else:  # gap
            a_seq1.append("-")
            a_seq2.append(seq2[y])
  
Would return:
    >>> alignment positions: [(7, 4), (6, 3), (5, 2), (4, 2)]
