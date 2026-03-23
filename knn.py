import math

def KClosest(element, data, k):
    #Initializing
    KClosestIndex = []
    KClosestDistance = []
    foundItFlag = False

    for i in range(len(data)):
        foundItFlag = False
        for j in range(len(KClosestIndex)):
            if(calc(element, data[i])<KClosestDistance[j] or KClosestDistance[j]==-1):
                KClosestIndex.insert(j, i)
                KClosestDistance.insert(j, calc(element, data[i]))
                foundItFlag = True
                break
            #This stops knn from tracking more rows than needed
            if(j>k):
                foundItFlag = True
                break
        if(not foundItFlag):
            KClosestIndex.append(i)
            KClosestDistance.append(calc(element, data[i]))
            foundItFlag = False
        
    return data, KClosestIndex, k


def checkNeighbors(data, closestData, k):
    # I'm making two lists, for the two different classes, and inserting the first value on the list of closest neighbors, into the first class (arbitrary choice)
    # In the end, what matters is which list is larger
    classOne = [] 
    classTwo = []
    classOne.append(data[closestData[0]][0])

    for i in range(1, k):
        print("Class One ", classOne, " Class Two ", classTwo)

        if classOne[0] == data[closestData[i]][0]:
            classOne.append(data[closestData[i]][0])
        else:
            classTwo.append(data[closestData[i]][0])
    
    if(len(classOne) > len(classTwo)):
        return chr(classOne[0])
    else:
        return chr(classTwo[0])


def calc(main, nearest):
    dist = math.sqrt((main[0] - nearest[1])**2 + (main[1] - nearest[2])**2 + (main[2] - nearest[3])**2 + (main[3] - nearest[4])**2 + (main[4] - nearest[5])**2 + (main[5] - nearest[6])**2 + (main[6] - nearest[7])**2 + (main[7] - nearest[8])**2 + (main[8] - nearest[9])**2 + (main[9] - nearest[10])**2 + (main[10] - nearest[11])**2 + (main[11] - nearest[10])**2 + (main[12] - nearest[13])**2 + (main[13] - nearest[14])**2 + (main[14] - nearest[15])**2 + (main[15] - nearest[16])**2 + (main[16] - nearest[17])**2 + (main[17] - nearest[18])**2 + (main[18] - nearest[19])**2 + (main[20] - nearest[19])**2 + (main[21] - nearest[20])**2 + (main[21] - nearest[22])**2)
    return dist