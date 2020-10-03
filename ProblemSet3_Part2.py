# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:34:07 2020

@author: sl559
"""
#%% Task 4.1 

#Create a Python file object, i.e., a link to the file's contents
fileObj = open('./transshipment_vessels_20180723.csv','r')

#Read the entire contents into a list object
lineList = fileObj.readlines()


#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)


#%% Task 4.2
#Split the headerLineString into a list of header items
headerItems = headerLineString.split(",")
print(headerItems)

#List the index of the mmsa, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)
#%% Task 4.3
#Create an empty dictionary
vesselDict = {}
lineList = lineList[1:]

#Iterate through all lines (except the header) in the data file:
for lineString in lineList:
#Split the data into values
    lineItems = lineString.split(",")
#Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineItems[mmsi_idx]
#Extract the fleet value
    fleet = lineItems[fleet_idx]
#Adds info to the vesselDict dictionary
    vesselDict[mmsi] = fleet
    
print(len(vesselDict))

#%% Task 4.4
vesselID= "258799000"
fleet_name = vesselDict[vesselID]
print (fleet_name)
print(f"Vessel # {vesselID} flies the flag of {fleet_name}")


#%% Task 5




























