#import DOM  and matplotlib
from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt

DOMTree=xml.dom.minidom.parse("go_obo.xml")#get the xml file
rootelement=DOMTree.documentElement#get the root element
term=rootelement.getElementsByTagName("term")

#get the total number of childnodes across all DNA-associated terms
DNA=0
for i in range(term.length):
    if "DNA" in term[i].getElementsByTagName("defstr")[0].childNodes[0].data:#find text in defstr that contains the word DNA
        DNA+=term[i].childNodes.length
print('The number of childNodes associated with "DNA" is ',str(DNA))

#get the total number of childnodes across all RNA-associated terms
RNA=0
for i in range(term.length):
    if "RNA" in term[i].getElementsByTagName("defstr")[0].childNodes[0].data:#find text in defstr that contains the word RNA
        RNA+=term[i].childNodes.length
print('The number of childNodes associated with "RNA" is ',str(RNA))

#get the total number of childnodes across all protein-associated terms
protein=0
for i in range(term.length):
    if "protein" in term[i].getElementsByTagName("defstr")[0].childNodes[0].data:#find text in defstr that contains the word protein
        protein+=term[i].childNodes.length
print('The number of childNodes associated with "protein" is ',str(protein))

#get the total number of childnodes across all glycoprotein-associated terms
glycoprotein=0
for i in range(term.length):
    if "glycoprotein" in term[i].getElementsByTagName("defstr")[0].childNodes[0].data:#find text in defstr that contains the word glycoprotein
        glycoprotein+=term[i].childNodes.length

print('The number of childNodes associated with "glycoprotein" is ',str(glycoprotein))

#print the pie chart
labels='DNA','RNA','protein','glycoprotein'#define the labels
sizes=[DNA,RNA,protein,glycoprotein]#get the sizes of each part
explode=(0,0,0,0.1)#the fourth macromolecule is highlighted as glycoprotein is chosen by myself
plt.pie(sizes,
        explode=explode,
        labels=labels,
        autopct='%1.1f%%',
        shadow=False,
        startangle=90)
plt.axis('equal')
plt.title('the pie chart of the number of childNodes associated with DNA, RNA, protein and glycoprotein')
plt.show()#show the pie chart
