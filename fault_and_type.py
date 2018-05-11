# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:13:54 2018

@author: Prashant
"""

### Road-user data
FaultType = pd.read_csv('datafile_4.csv')
FaultType = FaultType.drop(FaultType.index[[34,37]])


faulttype = {}
faulttype["Driver's Fault"] = FaultType.loc[36,'Fault of Driver-Total No. of Road Accidents - 2014'] 
faulttype["Cyclist's Fault"] = FaultType.loc[36,'Fault of Cyclist-Total No. of Road Accidents - 2014'] 
faulttype["Vehicle Condition"] = FaultType.loc[36,'Defect in Condition of Motor Vehicle-Total No. of Road Accidents - 2014'] 
faulttype["Road Condition"] = FaultType.loc[36,'Defect in Road Condition-Total No. of Road Accidents - 2014'] 
faulttype["Weather Condition"] = FaultType.loc[36,'Weather Condition-Total No. of Road Accidents - 2014'] 
faulttype["Passenger's Fault"] = FaultType.loc[36,'Fault of Passenger-Total No. of Road Accidents - 2014'] 
faulttype["Poor Light"] = FaultType.loc[36,'Poor light-Total No. of Road Accidents - 2014'] 
faulttype["Stray Animals"] = FaultType.loc[36,'Stray animals-Total No. of Road Accidents - 2014'] 
faulttype["Others"] = FaultType.loc[36,'Other causes/ Causes not known-Total No. of Road Accidents - 2014'] 


val = list(faulttype.values())
total = sum(val)
for i in range(0,9):
    val[i] = format(val[i]*100/total,'.2f')

plt.figure(figsize=(10,8))
plt.pie(list(faulttype.values()))
plt.axis('equal')
plt.xlabel('Accidents in 2014')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
label = [list(pair) for pair in zip(list(faulttype.keys()),val)]
plt.legend(label,loc="best")
plt.show()

# Involvement of different types of vehicles
RoadUserDf = pd.read_csv('datafile_3.csv')
if RoadUserDf.loc[['Telangana',12]] == "nan":
    print(1)

vehicletype = {}
vehicletype["2-Wheeler"] = RoadUserDf.loc[36,'Motor Cycle/ Scooter - Number of Road Accidents - Total - 2016']
vehicletype["2-Wheeler"] += RoadUserDf.loc[36,'Moped/Scootty - Number of Road Accidents - Total - 2016']

vehicletype["3-Wheeler"] = RoadUserDf.loc[36,'Auto rickshaw - Number of Road Accidents - Total - 2016']
vehicletype["3-Wheeler"] += RoadUserDf.loc[36,'Tempo - Number of Road Accidents - Total - 2016']
vehicletype["3-Wheeler"] += RoadUserDf.loc[36,'E-Rickshaw - Number of Road Accidents - Total - 2016']


vehicletype["4-Wheeler"] = RoadUserDf.loc[36,'Motor Car - Number of Road Accidents - Total - 2016']
vehicletype["4-Wheeler"] += RoadUserDf.loc[36,'Jeep - Number of Road Accidents - Total - 2016']
vehicletype["4-Wheeler"] += RoadUserDf.loc[36,'Taxi - Number of Road Accidents - Total - 2016']

vehicletype["Heavy Vehicle"] = RoadUserDf.loc[36,'Bus - Number of Road Accidents - Total - 2016']
vehicletype["Heavy Vehicle"] += RoadUserDf.loc[36,'Truck/Lorry - Number of Road Accidents - Total - 2016']
vehicletype["Heavy Vehicle"] += RoadUserDf.loc[36,'Articulated Vehicle/Trolly - Number of Road Accidents - Fatal - 2016']
vehicletype["Heavy Vehicle"] += RoadUserDf.loc[36,'Tractor - Number of Road Accidents - Total - 2016']

vehicletype["Other Vehicle"] = RoadUserDf.loc[36,'Other Motor Vehicles - Number of Road Accidents - Total - 2016']

#plot vehicle-type

plt.figure(figsize=(10,8))
plt.pie(list(vehicletype.values()),labels=list(vehicletype.keys()),autopct='%1.2f%%')
plt.axis('equal')
plt.xlabel('Types of Vehicles Involved in Accidents in 2016')

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.show()

