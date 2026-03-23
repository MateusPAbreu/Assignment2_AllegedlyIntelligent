import knn

# Data preprocessing
def readFile():
    fileName = open("MushroomData_8000.txt")
    info = []
    for lines in fileName:
        info.append(lines.rstrip(',\n'))
    splitData(info)

def splitData(data):
    train = []
    test = []
    answer = []
    check = 1 # to facilitate the split of data. A value of 1 gives training = 5600 and testing = 2400
    trainSplit = 0.7 # 5600 lines of data will be kept for training
    trainAmount = len(data) * trainSplit #
    #gotta check if the conversion to numbers should happen HERE or in KNN. I feel like it should be here
    for i in data:
        b = list(map(ord, i)) #ord returns the number representing the unicode code of a specified character, my only concern is how this might affect the '?' character
        # print(b)
        if check <= trainAmount:
            train.append(b)
        else:
            answer.append(b[0])
            test.append(b[1:])
        check = check+1
    c = train[1]
    # print(c[1])
    #knn.knn(train, 5)
    knn.KClosest(train[157], train, 5)
    return train, test, answer

def main():
    readFile()


if __name__ == "__main__":
    knn 
    main()