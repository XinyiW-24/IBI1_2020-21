def reverse(s):
#put cases of converted and original letters into a dictionary
    letter={'A':'T',
       'T':'A',
       'G':'C',
       'C':'G',
       'a':'T',
       't':'A',
       'g':'C',
       'c':'G'
       }
    convert=''
    seq=list(s)#change the string "s" into a list
    for i in range(len(s)):
        x=seq[len(s)-i-1]#read the original sequence from the back forward
        convert+=letter[x]#add converted letters to the "convert"

    return convert#return

#example
print(reverse('ATccGgat'))
