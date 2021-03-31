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
seq='ATGCGACTACGATCGAGGGCC'
protein=''
for i in range(0,len(seq),3):#translate each 3 codes to amino acid
	protein=protein+amino_acid[seq[i:i+3]]#add amino_acid to the string called protein
	
print(protein)#print out the amino acid
