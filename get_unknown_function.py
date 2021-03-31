import os
import re
os.chdir('C:\\Users\\wxy')
file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
lines=file.readlines()

unknown_function=[]
seq=[]
DNA=''
for i in range(len(lines)):
	if lines[i].startswith('>') and re.search(r'unknown function',lines[i]):
		name=re.findall(r'>(.+)_mRNA',lines[i])
		unknown_function.append(name)
	elif lines[i].stratswith('ATG\s+'):
		DNA=''
		for j in range(i,len(lines)):
			if lines[j].startswith('>'):
				break
			else:
				DNA=DNA+lines[j]+'\n'
		seq.append(DNA)

print(unknown_function)