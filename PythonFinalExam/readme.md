#Python Final Exam - US Pollution DataSet

#Pre-Analysis Script
Execution of this script will clean the data and structure the data in the form Folders based on State

        Usage : Pre_Analysis_Script.py
        
        Clean - Outliers
        ![Alt text](/DataAnalysisUsingPython/blob/master/PythonFinalExam/Screenshots/Screen%20Shot1.png)
        
        Create Folder Structure Based on States
        

#Analysis 1 - Average Gas Emitted per month expressed in percentage
Provides a heat map with months on the x-axis and the percent of emission of the gases like NO2, SO2, O3 and CO in y-axis
        
        Usage : Analysis1.py
        

#Analysis 2 - Recommending State for the specified Gas emission values - KNN Algorithm
User specifies the input value of 4 gases, the algorithm will determine the best possible state for these gases emission specified
        
        Usage : Analysis2.py 25.173913 0.5217390000000001 0.0135 0.617391
                (Analysis.py NO2Mean SO2Mean O3Mean COMean)
        
#Analysis 3 - Predict the gases mean in future - Based on Linear regression
User provides the year and month in (yyyymm) for which they need prediction, linear regression algorithm provides the emission of these gases along with a map which shows the linear spread of these gases
        
        Usage : Analysis3.py 201703
                (Analysis3.py yyyymm)

#Analysis 4 - Find Air Quality Index for a state and a particular year. 
User provides the state and year for which the air quality index for the gases is needed. The script iterates through the folder based on state and looks through the file with the name State_Year
        
        Usage : Analysis4.py Arizona 2015
                (Aanalysis4.py State yyyy)
