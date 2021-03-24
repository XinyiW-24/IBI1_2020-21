import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#The code for importing the .csv file
os.chdir("C:\\Users\\wxy")                           
covid_data=pd.read_csv("full_data.csv")                                                     #import the full_data.csv


#show all columns, and every second row between (and including) 0 and 10
covid_data.iloc[0:11:2,:]


#use Boolean to show "total_cases" for all rows corresponding to Afghanistan
Afghanistan=[]                                                                               #create an empty list
for i in range (0,7996) :                                                                    #use "for" to find "Afghanistan"
     if covid_data.iloc[i,1]=="Afghanistan" :
             Afghanistan.append(True)
     else:
             Afghanistan.append(False)

covid_data.loc[Afghanistan,"total_cases"]                                                    #show "total_cases" for all rows corresponding to Afghanistan


#compute the mean and median of new cases for the entire world
world=[]                                                                                     #create an empty list
for i in range (0,7996) :                                                                    #use "for" to find "world"
     if covid_data.iloc[i,1]=="World" :
             world.append(True)
     else:
             world.append(False)

world_new_cases=np.array(covid_data.loc[world,"new_cases"])    
np.mean(world_new_cases)                                                                     # The mean of new cases
np.median(world_new_cases)                                                                   #The median of new cases


#create a boxplot of new cases worldwide
plt.boxplot(world_new_cases,  #create a boxplot
             vert=True,
             whis=1.5,
             patch_artist=True,
             meanline=False,
             showbox=True,
             showcaps=True,
             showfliers=True,
             notch=False,
             )
plt.xlabel('new cases worldwide')                                                           #set the name of x-axis
plt.ylabel('number')                                                                        #set the name of y-axis
plt.title('new cases worldwide')                                                            #set the title
plt.show()                                                                                  #show boxplot


#plot both new cases and new deaths worldwide
world_new_cases=covid_data.loc[world,"new_cases"]    
world_new_deaths=covid_data.loc[world,"new_deaths"]
world_dates=covid_data.loc[world,"date"]

plt.plot(world_dates, world_new_cases,'b-',label='new cases')                               #set the points and legend
plt.plot(world_dates, world_new_deaths,'r-',label='new deaths')                             #set the points and legend
plt.legend()                                                                                #show the legend
plt.ylabel('number')                                                                        #set the name ofy-axis
plt.xlabel('date')                                                                          #set the name of x-axis
plt.title('new cases and new deaths worldwide')                                             #set the title
plt.yticks(np.arange(0,90000,5000))                                                         #set the y-axis
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-50)                             #set the x-axis
plt.show()                                                                                  #show the plot


#answer the question stated in file question.txt
Spain=[]                                                                                    #create an empty list
for i in range (0,7996) :                                                                   #use "for" to find "Spain"
     if covid_data.iloc[i,1]=="Spain" :      
             Spain.append(True)
     else:
             Spain.append(False)

Spain_new_cases=covid_data.loc[Spain,"new_cases"]
Spain_total_cases=covid_data.loc[Spain,"total_cases"]
Spain_dates=covid_data.loc[Spain,"date"]

plt.plot(Spain_dates, Spain_new_cases,'b-', label='new cases in Spain')                    #set the points and legend
plt.plot(Spain_dates, Spain_total_cases,'r-', label='total cases in Spain')                #set the points and legend
plt.ylabel('number')                                                                       #set the label of y-axis
plt.xlabel('date')                                                                         #set the label of x-axis
plt.title('new cases and total cases in Spain')                                            #set the title
plt.yticks(np.arange(0,90000,10000))                                                       #set the y-axis
plt.xticks(Spain_dates.iloc[0:len(Spain_dates):4],rotation=-50)                            #set the x-axis
plt.legend()                                                                               #show the legend
plt.show()                                                                                 #show the plot
