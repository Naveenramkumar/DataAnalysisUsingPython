
# coding: utf-8

# In[ ]:

#Analysis-1 : Average Gas Emitted Per Month expressed in Percentage
import calendar
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")

gasEmmisionPerMonth=pd.DataFrame()

for m in list(df["month"].unique()):
    for l in ["NO2Mean","COMean","SO2Mean","O3Mean"]:
        
        #monthInt = m.apply(lambda x:datetime.strptime(x,'%Y-%m-%d').date().strftime('%m'))
        #monthInt=calendar.month_abbr[m]
        monthInt=list(calendar.month_abbr).index(m)
        z=df[df["month"] == m][l].sum()
        x=df[l].sum()
        y=(z*100)/x
        gasEmmisionPerMonth=gasEmmisionPerMonth.append(pd.DataFrame({"gases": l,"month":monthInt,"averageEmission":y}, index=[0]))
       
gasEmmisionPerMonth = gasEmmisionPerMonth.pivot("gases","month","averageEmission")
fig, ax = plt.subplots(figsize=(20,5))
ax = sns.heatmap(gasEmmisionPerMonth, linewidth=1, annot=True)
monthStr = []
for i in range(1,len(df["month"].unique())+1):
    monthStr.append(calendar.month_abbr[i])
ax.set_xticklabels(monthStr,rotation=30)
plt.savefig("/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis1_Output.png")
print("Average Gas Emitted per Month")

