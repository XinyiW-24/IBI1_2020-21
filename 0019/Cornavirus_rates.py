import matplotlib.pyplot as plt
import numpy as np

cases={ 'USA':29967939, 'India':11305979, 'Brazil':11284269, 'Russia':4360823, 'UK':4241677}
labels= 'USA', 'India', 'Brazil', 'Russia', 'UK'

#calculate percentages
number=np.array([cases['USA'],cases['India'], cases['Brazil'], cases['Russia'], cases['UK']])
sizes=number/61160687*100

#draw pie
explode=(0.1, 0, 0, 0, 0)
colors=['yellow','green','red','blue','purple']
plt.pie(sizes, #Specify the data to plot the boxplot
	explode=explode, #Specify the number of slices in the pie chart
	labels=labels, #Specify labels
	colors=colors,
	autopct='%1.1f%%', #set format of numbers
	shadow=False, #set shadow
	startangle=90 
	)
plt.axis('equal')
plt.show()