#%% task1
mountain = "Denali"
nickname = '"Mt. McKinley"'
elevation = "20322" 

print (mountain + ", formerly \nknown as "  + nickname)
print ("is " + elevation + "' above sea level." )

#%% task2
#open the target file
dataFolder = "W:\859_data\tri_state"

#Creates a list object called dataList
dataList = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]

userItem = "streams.shp"

#Adds the userItem string object to the dataList list
dataList.append(userItem)

for dataString in dataList:
    print(dataFolder+"\\"+dataString)

#%% 



 
