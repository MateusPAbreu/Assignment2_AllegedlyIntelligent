import knn

# Data preprocessing
def readFile():
    fileName = open("MushroomData_8000.txt")
    info = []
    for lines in fileName:
        info.append(lines.rstrip('\n').replace(",",""))
    return info

def readUnknownData():
    fileName = open("MushroomData_Unknwon_100.txt")
    info = []
    unknownData = []
    for lines in fileName:
        info.append(lines.rstrip('\n').replace(",",""))
    for i in info:
        unknownData.append(list(map(ord, i)))
    return unknownData

def splitData(data):
    train = []
    test = []
    answer = []
    check = 1 # to facilitate the split of data. A value of 1 gives training = 5600 and testing = 2400
    trainSplit = 0.7 # 5600 lines of data will be kept for training
    trainAmount = len(data) * trainSplit #
    for i in data:
        b = list(map(ord, i)) #ord returns the number representing the unicode code of a specified character, my only concern is how this might affect the '?' character
        if check <= trainAmount:
            train.append(b)
        else:
            answer.append(b[0])
            test.append(b[1:])
        check = check+1

    return train, test, answer

def main():
    attributeClass = []
    info = readFile()
    unknownData = readUnknownData()
    train, test, answer= splitData(info)
    f = open("predictionResultKNN.txt", "w")
    for i in range(len(unknownData)):
        data, KClosestIndex, k = knn.KClosest(unknownData[i], train, 10)
        print(knn.checkNeighbors(data, KClosestIndex, k))
        f.write(knn.checkNeighbors(data, KClosestIndex, k) +'\n')


if __name__ == "__main__":
    knn 
    main()