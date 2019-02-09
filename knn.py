#########
#
# Creator : anshulTalati
# when: 02/08/2019 
#
#########

import math

D=[(170, 57, 32, 'W'), (192, 95, 28, 'M'), (150, 45, 30, 'W'), (170, 65, 29, 'M'), (175, 78, 35, 'M'), (185, 90, 32, 'M'), (170, 65, 28, 'W'), (155, 48, 31, 'W'), (160, 55, 30, 'W'), (182, 80, 30, 'M'), (175, 69, 28, 'W'), (180, 80, 27, 'M'), (160, 50, 31, 'W'), (175, 72, 30, 'M')]


while True:
    #Input the data point for prediction.
    input = raw_input("Please input a data point for the prediction as: height weight age OR -1 to Exit the Program \n")

    if input == '-1':
        break
    
    inputPoint = map(int, input.split())
    l = len(D)
    classList = []
    for i in range(l):
        if D[i][3] not in classList:
            classList.append(D[i][3])
    print classList

    # To choose Question data set with age.
    choice = int(raw_input("PLease type 1 for Prediction with age or 2 for Prediction without age>>> "))
    distList = []
    if choice == 1:
        # To calcualte the cartesian distance of the data point with the training data set with age
        for i in range(l):
            cartesianDistance = math.sqrt(((D[i][0]-inputPoint[0])**2) + ((D[i][1]-inputPoint[1])**2) + ((D[i][2]-inputPoint[2])**2))
            elem = (D[i], cartesianDistance)
            distList.append(elem)
    elif choice == 2:
        # To calcualte the cartesian distance of the data point with the training data set without age 
        for i in range(l):
            cartesianDistance = math.sqrt(((D[i][0]-inputPoint[0])**2) + ((D[i][1]-inputPoint[1])**2))
            elem = (D[i], cartesianDistance)
            distList.append(elem)

    #function to select the 2nd element for sorting. 
    def Second(element):
        return element[1]
    distList.sort(key=Second)

    print '\n'
    print 'Training data point sorted by their cartesian distance with datapoint'
    for i in range(len(distList)):
        print distList[i]

    # for Predicting the gender based on different nearest neighbour.
    while (True):
        mcount = 0
        wcount = 0 

        # Ask user for the number of neighbours for prediction 
        k= int(raw_input("\nPlease input the number of nearest neighbour factor i.e k OR input '-1' to try differnt data point \n"))
        print '\n'

        if k == -1:
            break
        
        # Print the nearest neighbours 
        print "The Nearest neighbours of data point are:\n"
        for i in range(k):
            print distList[i]

        for i in range(k):
            mcount = mcount + distList[i][0][3].count('M')
            wcount = wcount + distList[i][0][3].count('W')

        # Prediction Output to the User 
        if mcount > wcount:
            print "\nThe person is Male"
        else:
            print "\nThe person is Women "


    
