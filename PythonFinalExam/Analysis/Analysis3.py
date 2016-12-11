#Analysis 3: Predict the gases mean in future - Based on Linear regression
import matplotlib.pyplot as plt
import calendar
import pylab as pl
import pandas as pd
from datetime import datetime
import argparse
import sys
import csv
if len(sys.argv) != 2:
    print("Invalid call to the script : Please provide year and month in yyyymm format")
    sys.exit(2)

N=str(sys.argv[1])

if len(N) != 6:
    print("Invalid Input Provided. Please provide year and month in yyyymm format")
    sys.exit(2)
    
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
with open('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis3_Output.csv','w') as csvfile:
    writerrecord=csv.writer(csvfile, delimiter=',')
    writerrecord.writerow(['Gases','Predicted Emission'])
    writerrecord.writerow(['Predicted NO2Mean',findNO2(int(N))])

    writerrecord.writerow(['Predicted COMean',findCO(int(N))])

    writerrecord.writerow(['Predicted O3Mean',findO3(int(N))])

    writerrecord.writerow(['Predicted SO2Mean',findSO2(int(N))])



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
plt.savefig('/Users/Gany/Desktop/PythonFinalExam/OutputFiles/Analysis3Graph.png')
