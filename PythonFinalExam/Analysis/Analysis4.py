#Analysis 4 : Find Air Quality Index for a state and a particular year
import glob
import pandas as pd
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import numbers

if len(sys.argv) != 3:
    print("Invalid call to the script : Please provide State and Year in yyyy format")
    sys.exit(2)


df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")
stateProvided = str(sys.argv[1])
yearProvided = int(sys.argv[2])
dfs=pd.DataFrame
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
        pos = list(range(len(monthX)))
        width = 0.1

        # Plotting the bars
        fig, ax = plt.subplots(figsize=(10,5))
        plt.bar(pos,no2,width,alpha=0.5,color='r',label=monthX[0])
        plt.bar([p + width for p in pos],co,width,alpha=0.5,color='g',label=monthX[1])
        plt.bar([p + width*2 for p in pos],so2,width,alpha=0.5,color='b',label=monthX[2])
        plt.bar([p + width*3 for p in pos],o3,width,alpha=0.5,color='y',label=monthX[3])
        ax.set_ylabel('Air Quality Index')
        ax.set_xlabel('Month')
        # Set the chart's title
        ax.set_title('Air Quality Index')

        # Set the position of the x ticks
        ax.set_xticks([p + 1.5 * width for p in pos])

        # Set the labels for the x ticks
        ax.set_xticklabels(monthX)

        # Setting the x-axis and y-axis limits
        plt.xlim(min(pos)-width, max(pos)+width*4)
        #plt.ylim([0, max(no2,co,so2,o3)] )

        # Adding the legend and showing the plot
        plt.legend(['NO2 AQI','CO AQI','SO2 AQI','O3 AQI'], loc='upper left')
        plt.grid()

        plt.savefig('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis4Graph.png')
    else:
        print("Invalid Year Provided")
        exit
else:
    print("Invalid State Provided")
    exit
