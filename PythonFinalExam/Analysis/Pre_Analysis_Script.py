
# coding: utf-8

# In[ ]:

#Pre-Analysis Script : Cleaning and Structuring Data
import pandas as pd
import subprocess
import os
from datetime import datetime
df=pd.read_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/USPollutionData.csv")

df["month"]=df["DateLocal"].apply(lambda x:datetime.strptime(x,'%Y-%m-%d').date().strftime('%b'))
df["year"]=df["DateLocal"].apply(lambda x:datetime.strptime(x,'%Y-%m-%d').date().strftime('%Y'))
df["monthyear"]=df["DateLocal"].apply(lambda x:datetime.strptime(x,'%Y-%m-%d').date().strftime('%Y%m'))
df = df[df["NO2Mean"] > 0]
df = df[df["SO2Mean"] > 0]
df = df[df["O3Mean"] > 0]
df = df[df["COMean"] > 0]
df = df[pd.to_numeric(df["year"]) > 2014]
df.to_csv("/Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv")
fileName = "/Users/Gany/Desktop/createFolders.sh"
file = open(fileName, "w")
rmCommand='''rm -rF /Users/Gany/Desktop/PythonProject \n'''
file.write(rmCommand)
baseString = "mkdir -p /Users/Gany/Desktop/PythonProject/"
for s in list(df["State"].unique()):
    newString = baseString + s + "\n"
    file.write(newString)
file.close()    
os.chmod('/Users/Gany/Desktop/createFolders.sh', 0o755)
scriptOutput = os.system('/Users/Gany/Desktop/createFolders.sh')
print("Folders Created NOW")
fileName1 = "/Users/Gany/Desktop/createFiles.sh"
file1 = open(fileName1,"w")
baseHeader='''head -1 /Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv '''
baseHeader1='''> /Users/Gany/Desktop/PythonProject/'''
baseString1 = '''cat /Users/Gany/Desktop/PythonFinalExam/InputFiles/PollutionDataModified.csv | awk -F',' '{if($6 == "'''
baseString2 = '''" && $31 == "'''
baseString3 = '''") print}' >> /Users/Gany/Desktop/PythonProject/'''
for s in list(df["State"].unique()):
    for y in list(df[df["State"]==s]["year"].unique()):
        
        newString1 = baseHeader + baseHeader1 +s+"/"+s + "_" + y +".csv \n" + baseString1 + s + baseString2 + y + baseString3 + s + "/" +s + "_" + y +".csv \n"
        file1.write(newString1)
file1.close()
print("Completed")
os.chmod('/Users/Gany/Desktop/createFiles.sh', 0o755)
os.system('/Users/Gany/Desktop/createFiles.sh')
print("Script Executed")

