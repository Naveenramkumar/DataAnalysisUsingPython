
# coding: utf-8

# In[ ]:

#Analysis 2 : Recommending State for the specified Gas emission values - KNN Algorithm
import calendar
import pandas as pd
from datetime import datetime
f2=open('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis2_Output.csv','w+')
df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")

distance1=10000;
distance2=10000;
distance3=10000;
state3=""
state2=""
state1=""
for i in df.index.values:
    distance = ((float(df.loc[i,"NO2Mean"])-25.173913)**2 + (float(df.loc[i,"SO2Mean"])-0.5217390000000001)**2 + (float(df.loc[i,"O3Mean"])-0.0135)**2 + (float(df.loc[i,"COMean"])-0.617391)**2)**(1/2)
    if distance1>distance:
        distance3=distance2
        distance2=distance1
        distance1=distance
        state3=state2
        state2=state1
        state1=df.loc[i,"State"]
    elif distance2>distance:
        distance3=distance2
        distance2=distance
        state3=state2
        state2=df.loc[i,"State"]
    elif distance3>distance:
        distance3=distance
        state3=df.loc[i,"State"]
f2.write('Term','State','Distance')               
f2.write('Closest State and distance : ',state1,'--->',distance1)

f2.write('Second Closest State and distance : ',state2,'--->',distance2)

f2.write('Third Closest State and distance : ',state3,'--->',distance3)
f2.close()


# In[ ]:



