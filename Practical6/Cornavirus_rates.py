import matplotlib.pyplot as plt
import numpy as np

cases={ 'USA':29967939, 'India':11305979, 'Brazil':11284269, 'Russia':4360823, 'UK':4241677}
labels= 'USA', 'India', 'Brazil', 'Russia', 'UK'
print(cases) #Displays frequency table
#calculate percentages
number=np.array([cases['USA'],cases['India'], cases['Brazil'], cases['Russia'], cases['UK']])
sizes=number/61160687*100

#draw pie chart which shows proportions of cases in different countries 
explode=(0.1, 0, 0, 0, 0)#highlight the USA section as it had the biggest number of cases
colors=['yellow','green','red','blue','purple']
plt.pie(sizes, #Specify the data to plot the boxplot
	explode=explode, #Specify the number of slices in the pie chart
	labels=labels, #Specify labels
	colors=colors,
	autopct='%1.1f%%', #set format of numbers
	shadow=False, #set shadow
	startangle=90 
	)
plt.title('Coronavirus infection rates across countries')
plt.axis('equal')
plt.show()
