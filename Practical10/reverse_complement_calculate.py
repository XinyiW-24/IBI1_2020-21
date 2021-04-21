def reverse(s):
    letter={'A':'T',
       'T':'A',
       'G':'C',
       'C':'G',
       'a':'T',
       't':'A',
       'g':'C',
       'c':'G'
       }
    revert=[]
    seq=list(s)
    for i in range(len(s)):
        x=seq[len(s)-i-1]
        revert.append(letter[x])

    return revert
print(reverse('ATccGgat'))