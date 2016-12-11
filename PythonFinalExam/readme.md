##Python Final Exam - US Pollution DataSet

#Pre-Analysis Script
Execution of this script will clean the data and structure the data in the form Folders based on State

        Usage : Pre_Analysis_Script.py
        
        Clean - Outliers - Mean value of emission of gases has negative values
        https://cloud.githubusercontent.com/assets/22332237/21077188/20f8b960-bf11-11e6-948b-ce9bbd508b45.png
        
        Create Folder Structure Based on States
        

#Analysis 1 - Average Gas Emitted per month expressed in percentage
Provides a heat map with months on the x-axis and the percent of emission of the gases like NO2, SO2, O3 and CO in y-axis
        
        Usage : Analysis1.py

** Observations **        
* Emission of gases like SO2 and NO2 are very high during Jan, Feb and Mar - Motor Vehicles run at high rate during this period
* Emission of O3 gas is very high during Mar, Apr, May - The harmful sun-rays penetrate and UV-Index is very hish causing skin problems during this period
        

#Analysis 2 - Recommending State for the specified Gas emission values - KNN Algorithm
* User specifies the input value of 4 gases, the algorithm will determine the best possible state for these gases emission specified
* Consider we have got a data of emission of gases for today and we are unable to find for which state the emission belongs.
* This Algorithm provides three closest points based on training dataset
        
        Usage : Analysis2.py 25.173913 0.5217390000000001 0.0135 0.617391
                (Analysis.py NO2Mean SO2Mean O3Mean COMean)

        Algorithm: Closest 3 states data considered for computation of KNN Algorithm
        for i in df.index.values:
                distance = ((float(df.loc[i,"NO2Mean"])-inp1)**2 + (float(df.loc[i,"SO2Mean"])-inp2)**2 + 
                (float(df.loc[i,"O3Mean"])-inp3)**2 + (float(df.loc[i,"COMean"])-inp4)**2)**(1/2)
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

#Analysis 3 - Predict the gases mean in future - Based on Linear regression
* User provides the year and month in (yyyymm) for which they need prediction for future.
* Linear regression algorithm provides the emission of these gases for the provided month and year. 
* Map which shows the linear spread of these gases is also generated
        
        Usage : Analysis3.py 201703
                (Analysis3.py yyyymm)
                
        Algorithm : Linear Regression
                Calculate Variance and Co-Variance
                Compute slope = Co-Variance(A,B)/Variance(A)
                Compute constant : c = y - mx with x and y as their respective mean values

#Analysis 4 - Find Air Quality Index for a state and a particular year. 
* User provides the state and year for which the air quality index for the gases is needed. 
* The script iterates through the folder based on state and looks through the file with the name State_Year.csv
        
        Usage : Analysis4.py Arizona 2015
                (Aanalysis4.py State yyyy)
