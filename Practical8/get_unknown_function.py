import os
import re
os.chdir('C:\\Users\\wxy\\IBI1_2020-21\\Practical8\\')
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')#open the file
lines=file.readlines()

#put names and sequence into different lists
names=[]
seq=[]
length=[]

for i in range(len(lines)):
    if lines[i].startswith('>') and re.search(r'unknown function',lines[i]):#find the line which has name of DNA
        name=re.findall(r'>(.+)_mRNA',lines[i])#find the name 
        names.append(name[0])#add name to list called names
    elif lines[i-1].startswith('>')and re.search(r'unknown function',lines[i-1]):#find the first line of DNA sequence
        DNA=''#empty the string called DNA
        for j in range(i,len(lines)):#add the following lines of DNA sequence to the same string called DNA
            if lines[j].startswith('>'):
                break
            else:
                line=re.sub(r'\n','',lines[j])#remove'\n'
                DNA=DNA+line
        seq.append(DNA)#add DNA to list called seq
        
for i in range(len(seq)):
    l=len(seq[i])
    length.append(l)
x=''

for i in range(len(seq)):#combine the two lists (seq and names) together 
    x=x+str(names[i])
    n=20-len(names[i])
    for j in range(n):#add blankspace between name and length
        x=x+' '
    x=x+str(length[i])+'\n'+str(seq[i])+'\n'
    
#write name,length,sequence to a file
f=open('unknown_function.fa','w')
f.write(x)#write x into the file
file.close#close file
f.close#close f
