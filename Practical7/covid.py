import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#The code for importing the .csv file
os.chdir("C:\\Users\\wxy")
covid_data=pd.read_csv("full_data.csv")


#show all columns, and every second row between (and including) 0 and 10
covid_data.iloc[0:11:2,:]


#use Boolean to show "total_cases" for all rows corresponding to Afghanistan
Afghanistan=[]
for i in range (0,7996) :
     if covid_data.iloc[i,1]=="Afghanistan" :
             Afghanistan.append(True)
     else:
             Afghanistan.append(False)

covid_data.loc[Afghanistan,"total_cases"]


#compute the mean and median of new cases for the entire world
world=[]
for i in range (0,7996) :
     if covid_data.iloc[i,1]=="World" :
             world.append(True)
     else:
             world.append(False)

world_new_cases=np.array(covid_data.loc[world,"new_cases"])
np.mean(world_new_cases)  # The mean of new cases
np.median(world_new_cases) #The median of new cases


#create a boxplot of new cases worldwide
plt.boxplot(world_new_cases,
             vert=True,
             whis=1.5,
             patch_artist=True,
             meanline=False,
             showbox=True,
             showcaps=True,
             showfliers=True,
             notch=False,
             )
plt.xlabel('new cases worldwide')
plt.ylabel('number')
plt.title('new cases worldwide')
plt.show()


#plot both new cases and new deaths worldwide
world_new_cases=covid_data.loc[world,"new_cases"]
world_new_deaths=covid_data.loc[world,"new_deaths"]
world_dates=covid_data.loc[world,"date"]

plt.plot(world_dates, world_new_cases,'b-',label='new cases')
plt.plot(world_dates, world_new_deaths,'r-',label='new deaths')
plt.legend()
plt.ylabel('number')
plt.xlabel('date')
plt.title('new cases and new deaths worldwide')
plt.xticks(world_dates)
plt.yticks(np.arange(0,90000,5000))
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-50)
plt.show()


#answer the question stated in file question.txt
Spain=[]
for i in range (0,7996) :
     if covid_data.iloc[i,1]=="Spain" :
             Spain.append(True)
     else:
             Spain.append(False)

Spain_new_cases=covid_data.loc[Spain,"new_cases"]
Spain_total_cases=covid_data.loc[Spain,"total_cases"]
Spain_dates=covid_data.loc[Spain,"date"]

plt.plot(Spain_dates, Spain_new_cases,'b-', label='new cases in Spain')
plt.plot(Spain_dates, Spain_total_cases,'r-', label='total cases in Spain')
plt.ylabel('number')
plt.xlabel('date')
plt.title('new cases and total cases in Spain')
plt.xticks(Spain_dates)
plt.yticks(np.arange(0,90000,10000))
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-50)
plt.legend()
plt.show()