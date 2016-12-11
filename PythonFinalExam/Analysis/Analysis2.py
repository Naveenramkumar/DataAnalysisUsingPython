#Analysis 2 : Recommending State for the specified Gas emission values - KNN Algorithm
import calendar
import csv
import pandas as pd
from datetime import datetime
import sys
if len(sys.argv) != 5:
    print("Invalid call to script. \n Usage : python Analysis2.py 15.173913 3.52 6.01 1.61")
    
try:
    inp1 = float(sys.argv[1])
    inp2 = float(sys.argv[2])
    inp3 = float(sys.argv[3])
    inp4 = float(sys.argv[4])
except ValueError:
    print("Input is not a Float")
    sys.exit(2)
    
df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")

distance1=10000;
distance2=10000;
distance3=10000;
state3=""
state2=""
state1=""
for i in df.index.values:
    distance = ((float(df.loc[i,"NO2Mean"])-inp1)**2 + (float(df.loc[i,"SO2Mean"])-inp2)**2 + (float(df.loc[i,"O3Mean"])-inp3)**2 + (float(df.loc[i,"COMean"])-inp4)**2)**(1/2)
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
with open('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis2_Output.csv','w') as csvfile:
    writerrecord=csv.writer(csvfile, delimiter=',')
    writerrecord.writerow(['Index','State','Distance'])
               
    writerrecord.writerow(['Closest',state1,distance1])

    writerrecord.writerow(['Second Closest',state2,distance2])

    writerrecord.writerow(['Third Closest',state3,distance3])
