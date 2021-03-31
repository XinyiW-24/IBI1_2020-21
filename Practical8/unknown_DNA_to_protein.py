import os
import re
os.chdir('C:\\Users\\wxy\\IBI1_2020-21\\Practical8\\')
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open the file
lines=file.readlines()

#put names and sequence into different lists
names=[]
seq=[]

for i in range(len(lines)):
    if lines[i].startswith('>') and re.search(r'unknown function',lines[i]):#find the line which has name of DNA
        name=str(re.findall(r'>(.+)_mRNA',lines[i]))#find the name
        names.append(name)#add name to list called names
    elif lines[i-1].startswith('>')and re.search(r'unknown function',lines[i-1]):#find the first line of DNA sequence
        DNA=''#empty the string called DNA
        for j in range(i,len(lines)):#add the following lines of DNA sequence to the same string called DNA
            if lines[j].startswith('>'):
                break
            else:
                line=re.sub(r'\n','',lines[j])#remove'\n'
                DNA=DNA+line
        seq.append(DNA)#add DNA to list called seq
length=[]
for i in range(len(seq)):#count the lenth of each protein and add to a list called l
    l=int(len(seq[i])/3)
    length.append(l)
        
x=''

for i in range(len(seq)*2):
    if i%2==0:#add name and length to a string called x
        x=x+str(names[int(i/2)])
        n=20-len(names[int(i/2)])
        for j in range(n):
            x=x+' '
        x=x+str(length[int(i/2)])+'\n'
    else:#translate DNA to protein
        amino_acid={'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
                 'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
                 'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
                 'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
                 'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
                 'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
                 'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
                 'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
                 'TAT':'Y','TAC':'Y','TAA':'O','TAG':'U',
                 'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
                 'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
                 'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
                 'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
                 'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
                 'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
                 'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
                 }#the genetic code was from IBI1,2021
        s=str(seq[int((i-1)/2)])
        protein=''
        for d in range(0,len(seq[int((i-1)/2)]),3):#translate each 3 codes to amino acid
            protein=protein+amino_acid[s[d:d+3]]
        x=x+protein+'\n
f=open('C:\\Users\\wxy\\IBI1_2020-21\\Practical8\\unknown_function_protein.fa','w')
f.write(x)#write x into the file
file.close#close file
f.close#close f


