# K--Nearest-Neighbour-

# Description
* K-Nearest-Neighbors algorithm is used for classification and regression problems.
* In this project, it is used for classification 


## Data set format

* CSV (Comma Separated Values) format.
* Attributes can be integer or real values.
* List attributes first, and add response as the last parameter in each row.
    * E.g. 170 , 55 , 35, "M" where the first 3 numbers are values of attributes height, weight, age and "M" is one of the response classes.

* Responses can be integer, real or categorical.
* Training data set is directly in the program code, To check the program with different training data please edit it directly in the code mainting the format.
* Data set used in this code is 
        * D = [(170, 57, 32, 'W'), (192, 95, 28, 'M'), (150, 45, 30, 'W'), (170, 65, 29, 'M'), (175, 78, 35, 'M'), (185, 90, 32, 'M'), (170, 65, 28, 'W'), (155, 48, 31, 'W'), (160, 55, 30, 'W'), (182, 80, 30, 'M'), (175, 69, 28, 'W'), (180, 80, 27, 'M'), (160, 50, 31, 'W'), (175, 72, 30, 'M')]
    
* Format of the data set (height, weight, Age, "class')

## How to Run the code 

1. Run the file by using command "python knn.py"
2. Enter the data point to be predicted(eg "155 40 35"), 
    User also has the option to exit the program by inputing -1
3. Input 1 For prediction considering the age parameter (Question 2b) OR
    Input 2 For prediction without considering the age parameter(Question 2c)
4. Cartesian distance as the similarity measurements is used for  gender prediction
5. The Screen will show the intermediate step with the training data sorted by their cartesian distance from input data point 
    
    Cartesian distance caluation:

    Considering Age: 

    distance = sqrt((height- inputHeight)^2 + (weight- inputWeight)^2 + (age - inputAge)^2 )

    height, weight, age are the feature of the training data set 
    
    Not Considering Age:

    distance = sqrt((height- inputHeight)^2 + (weight- inputWeight)^2)

5. The program will then ask user to input number of neighbours(k value) to be considered for prediction.
6. The program will identify and display k nearest neighbour based on the cartesian distance.
    The prediction of the Data point is also be made based on the highest number of nearest neighbour of particular class.

7. User will be asked whether to exit the program by inputing -1 or to conduct the prediction using different K value.

8. to exit the program keep inputing -1

