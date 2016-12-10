
# coding: utf-8

# In[12]:

#Analysis 4 : Find Air Quality Index for a state and a particular year
import glob
import pandas as pd
import calendar
from datetime import datetime
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")
stateProvided = "Arizona"
yearProvided = 2015
dfs=""
if stateProvided in df["State"].unique():
    if yearProvided in df[df["State"] == stateProvided]["year"].unique():
        
        path="/Users/Gany/Desktop/PythonProject/"+stateProvided+"/"+stateProvided+"_"+str(yearProvided)+".csv"
        dfs=pd.read_csv(path)
        no2=[]
        co=[]
        so2=[]
        o3=[]
        monthX=[]
        for mon in dfs["month"].unique():
            m=list(calendar.month_abbr).index(mon)
            aqiNO2=dfs[dfs["month"]==mon]["NO2AQI"].mean()
            no2.append(aqiNO2)
            aqiCO=dfs[dfs["month"]==mon]["COAQI"].mean()
            co.append(aqiCO)
            aqiSO2=dfs[dfs["month"]==mon]["SO2AQI"].mean()
            so2.append(aqiSO2)
            aqiO3=dfs[dfs["month"]==mon]["O3AQI"].mean()
            o3.append(aqiO3)
            monthX.append(m)
            #print(mon,"-->",aqiNO2,"-->",aqiCO,"-->",aqiSO2,"-->",aqiO3)
            #ax = plt.subplot(111)
            #ax.bar(x-0.2, y,width=0.2,color='b',align='center')
        multiple_bars = plt.figure()
        
        ax = plt.subplot(111)
        ax.bar(monthX, no2,width=0.2,color='b',align='center')
        plt.xlabel("Months")
        plt.ylabel("NO2 AQI")
        plt.show()
    else:
        print("Invalid Year Provided")
        exit
else:
    print("Invalid State Provided")
    exit


# In[ ]:



