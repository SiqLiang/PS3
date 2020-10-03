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

#%% Task3.1
userNumbers = []
for x in range(3):
    userNumber= input("Enter an interger: ")
    userNumber_int = int(userNumber)
    userNumbers.append(userNumber_int)
    
userNumbers.sort()
print(userNumbers[-1])
 #%% Task3.2
userNumbers = []
for x in range(3):
    userNumber= input("Enter an interger: ")
    userNumber_int = int(userNumber)
    userNumbers.append(userNumber_int)
    
userNumbers.sort(reverse=True)
print(userNumbers)
 
