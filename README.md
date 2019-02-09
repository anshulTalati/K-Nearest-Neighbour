# K--Nearest-Neighbour-

Training data set is directly in the program code, To check the program with different training data please edit it directly in the code mainting the format.

Format of the data set (height, weight, Age, "class')


1. Run the file by using command "python knn.py"
2. Enter the data point to be predicted(eg "155 40 35"), 
    User also has the option to exit the program by inputing -1
3. Input 1 For prediction considering the age parameter (Question 2b) OR
    Input 2 For prediction without considering the age parameter(Question 2c)
4. The Screen will show the intermediate step with the training data sorted by their cartesian distance from input data point 
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

