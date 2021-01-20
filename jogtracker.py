#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:10:04 2021

@author: davidfordjour
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def Read_Two_Column_File(file_name):
    """Reading in the data for time and date."""
    with open(file_name, 'r') as data:
        x = []      # Creating empty lists for date and running times.
        times = []
        count = 0   # A line counter that starts at the top of the page
        
        for line in data:  
            count+=1    # Moving to the next line 
            d = line.split(" ")  #Indicating how columns are separated 
            times.append((d[0]))    #Data in first column goes into times list
            x.append(d[1])  #Data in second column goes into x-axis
    return x, times


x, times = Read_Two_Column_File('times.txt')  #Reading times.txt file  

def String_To_Minutes(time):
    """Converting strings in times-list to minutes."""
    if type(time) == bytes:
        time = time.decode()
    
    t = time.split(":") #Times are split with ":"
    minutes = (float(t[0])) + (float(t[1])*0.05/3) 
    return minutes
        

y_axis = []

for y in times:
    print(String_To_Minutes(y))
    y_axis.append(String_To_Minutes(y))


print(x)
#print(y)
plt.plot(x,y_axis)
plt.xlabel("Date")
plt.ylabel("Mins")
plt.title("jogging times")
