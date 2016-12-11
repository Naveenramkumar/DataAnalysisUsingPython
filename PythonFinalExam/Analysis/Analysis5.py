
# coding: utf-8

# In[ ]:

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")
hourMax=[]
hourAqi=[]
for i in df["O3FirstMaxHour"].unique():
    aqi=df[df["O3FirstMaxHour"]==i]["O3AQI"].mean()
    hourMax.append(i)
    hourAqi.append(aqi)

plt.plot(hourMax,hourAqi,'ro')
plt.ylabel('O3 AQI')
plt.xlabel('Hour of day')
plt.savefig("/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis5Graph.png")

