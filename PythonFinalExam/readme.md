#Python Final Exam - US Pollution DataSet

#Pre-Analysis Script
Execution of this script will clean the data and structure the data in the form Folders based on State

#Analysis 1 - Average Gas Emitted per month expressed in percentage
Provides a heat map with months on the x-axis and the percent of emission of the gases like NO2, SO2, O3 and CO in y-axis

#Analysis 2 - Recommending State for the specified Gas emission values - KNN Algorithm
User specifies the input value of 4 gases, the algorithm will determine the best possible state for these gases emission specified

#Analysis 3 - Predict the gases mean in future - Based on Linear regression
User provides the year and month for which they need prediction, linear regression algorithm provides the emission of these gases along with a map which shows the linear spread of these gases

#Analysis 4 - Find Air Quality Index for a state and a particular year
User provides the state and year for which the air quality index for the gases is needed. 
The script iterates through the folder based on state and looks through the file with the name State_Year
