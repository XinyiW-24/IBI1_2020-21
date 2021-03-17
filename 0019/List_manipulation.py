import numpy as np
import matplotlib.pyplot as plt

#Set gene_lengths and exon_counts as type array
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])

#Calculate average
average=list(gene_lengths/exon_counts)

#draw a boxplot
n=10
plt.boxplot(average, 
	vert=True, #Decide whether the boxplot should be placed vertically
	whis=1.5, #Decide the distance between the upper and lower quartiles
	patch_artist=True, #Fill the color of the box
	meanline=False, #Write the mean as a line
	showbox=True, #Show box of boxplot
	showcaps=True,#Show two lines at the top and end of a boxplot
	showfliers=True,#show outliers
	notch=False,
	boxprops={'color': 'blue','facecolor':'purple'} #set color
	)
plt.show()

