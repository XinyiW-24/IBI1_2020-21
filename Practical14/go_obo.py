#import DOM and matplotlib
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt

DOMTree=xml.dom.minidom.parse("go_obo.xml")#get the xml file
total=DOMTree.documentElement
terms=total.getElementsByTagName('term')


#identify id as key and is_a as value in a dictionary (one key can have more than one value)
idis={}
for n in terms:
	isa=n.getElementsByTagName('is_a')
	goid=n.getElementsByTagName('id')[0]
	for i in isa:
		if i.childNodes[0].data in idis:
			idis[i.childNodes[0].data].append(goid.childNodes[0].data)#add value
		else:
			idis[i.childNodes[0].data]=[goid.childNodes[0].data]#add key

#use this function to find the id of the terms about one kind of molecule
def find(molecule,Molecule,terms):
        L=[]
        for n in range (terms.length): #https://www.cnblogs.com/poloyy/p/12207464.html
                if molecule in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:#find text in defstr that contains the word "molecule"
                        L.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)
                elif Molecule in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:##find text in defstr that contains the word "Molecule" (in case the word is in the beginning of a sentence)
                        L.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)
        return L

DNA=find('DNA','DNA',terms)
RNA=find('RNA','RNA',terms)
protein=find('protein','Protein',terms)
carbohydrate=find('carbohydrate','Carbohydrate',terms)

#use a recursion to find the childnodes of terms
def nodenumber(idis,molelist):
	child=[]
	for i in molelist:
		if i in idis:
			childnode=idis[i]
			child+=childnode
			child+=nodenumber(idis,childnode)#recursion
	return child

#get the number of childnodes and use set() to avoid repetition
DNAlength=len(set(nodenumber(idis,DNA)))
RNAlength=len(set(nodenumber(idis,RNA)))
proteinlength=len(set(nodenumber(idis,protein)))
carbohydratelength=len(set(nodenumber(idis,carbohydrate)))

#print out the numbers
print('The number of childNodes of DNA-associated terms is ',str(DNAlength))
print('The number of childNodes of RNA-associated terms is ',str(RNAlength))
print('The number of childNodes of protein-associated terms is ',str(proteinlength))
print('The number of childNodes of carbohydrate-associated terms is ',str(carbohydratelength))

#print the pie chart
labels='DNA','RNA','protein','carbohydrate'#define the labels
sizes=[DNAlength,RNAlength,proteinlength,carbohydratelength]#get the sizes of each part
explode=(0,0,0,0.1)#the fourth macromolecule is highlighted as carbohydrate is chosen by myself
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.axis('equal')
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and carbohydrate')
plt.show()#show the pie chart
