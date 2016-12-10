
# coding: utf-8

# In[ ]:

#Analysis 3: Predict the gases mean in future - Based on Linear regression
import matplotlib.pyplot as plt
import calendar
import pylab as pl
import pandas as pd
from datetime import datetime
f3=open('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis3_Output.txt','w+')
df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")

def covariance(A,B):
    i=0
    sum=0
    for items in A:
        i+=1
        sum+=items
    if i!=0:
        meanA=sum/i;
    i=0
    sum=0
    for items in B:
        i+=1
        sum+=items
    if i!=0:
        meanB=sum/i;
    
    cov=0.0
    for i in range(0,len(A)):
        cov+=(A[i]-meanA)*(B[i]-meanB);
    cov=cov/(len(A)-1)
    return cov

def variance(A):
    i=0
    sum=0
    for items in A:
        i+=1
        sum+=items
    if i!=0:
        meanA=sum/i;
    variance=0.0
    
    for i in range(0,len(A)):
        variance+=(A[i]-meanA)**2
    variance=variance/(len(A)-1)
    return variance

def LinearRegressionSlope(A,B):
    return (float)(covariance(A,B)/variance(A))

def LinearRegressionConstant(A,B):
    i=0
    sum=0
    for items in A:
        i+=1
        sum+=items
    if i!=0:
        meanA=sum/i;
    i=0
    sum=0
    for items in B:
        i+=1
        sum+=items
    if i!=0:
        meanB=sum/i;
    
    return meanB-(meanA*LinearRegressionSlope(A,B))



def findNO2(year):
    a=list(df["monthyear"].astype(int).unique())
    b=[]

    for i in (list(df["monthyear"].unique())):
        b.append(df[df["monthyear"]==i]["NO2Mean"].mean())
    slope=LinearRegressionSlope(a,b)
    constant=LinearRegressionConstant(a,b)
    return (slope*year)+constant

def findSO2(year):
    a=list(df["monthyear"].astype(int).unique())
    b=[]
    for i in (list(df["monthyear"].unique())):
        b.append(df[df["monthyear"]==i]["SO2Mean"].mean())
    slope=LinearRegressionSlope(a,b)
    constant=LinearRegressionConstant(a,b)
    return (slope*year)+constant

def findO3(year):
    a=list(df["monthyear"].astype(int).unique())
    b=[]
    for i in (list(df["monthyear"].unique())):
        b.append(df[df["monthyear"]==i]["O3Mean"].mean())
    slope=LinearRegressionSlope(a,b)
    constant=LinearRegressionConstant(a,b)
    return (slope*year)+constant

def findCO(year):
    a=list(df["monthyear"].astype(int).unique())
    b=[]
    for i in (list(df["monthyear"].unique())):
        b.append(df[df["monthyear"]==i]["COMean"].mean())
    slope=LinearRegressionSlope(a,b)
    constant=LinearRegressionConstant(a,b)
    return (slope*year)+constant

f3.write('The Predicted NO2Mean at the given year : ')
f3.write(findNO2(201703))
f3.write('The Predicted COMean at the given year : ')
f3.write(findCO(201703))
f3.write('The Predicted O3Mean at the given year : ')
f3.write(findO3(201703))
f3.write('The Predicted SO2Mean at the given year : ')
f3.write(findSO2(201703))


a=list(df["monthyear"].astype(int).unique())
b=[]

for i in (list(df["monthyear"].unique())):
    b.append(df[df["monthyear"]==i]["NO2Mean"].mean())
    
c=[]
for items in a:
    mont=items%100
    #month=datetime.date(1900,mont,1).strftime('%b')
    monthe=calendar.month_abbr[mont]
    year=int(items/100)
    monthyear=str(monthe)+str(year)
    c.append(monthyear)

d=[]
for items in range(1,len(c)+1):
    d.append(items)
fig, ax = plt.subplots()
    
plt.plot(d, b, 'ro')
plt.xticks(d,c,rotation='vertical')
plt.ylabel('NO2Mean')



ax.plot([d[0],d[len(d)-1]], [findNO2(a[0]),findNO2(a[len(a)-1])], c='b')
plt.show()


# In[ ]:



