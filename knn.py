import math

def knn(data, k):
    for i in range(len(data)): 
        main = data[i]
        # FIXES THIS NEEDS: 
        # Right now it breaks because, when it reaches the last element, I think I should go back to look at the neighbors above.
        # at the moment I'm only considering the items below the current item, have to change that to consider those above it too.
        for j in range(k):
            if i+j >= len(data):
                #do something
                nearest = data[i+1]
            else:
                nearest = data[i+j]
            print(i, j, len(data))
            #should probably get the result, compare what's the highest and then determine if it's poisonous or edible based on that
        # print(main, nearest)

def calc(main, nearest):
    dist = math.sqrt((main[1] - nearest[1])**2 + (main[2] - nearest[2])**2 + (main[3] - nearest[3])**2 + (main[4] - nearest[4])**2 + (main[5] - nearest[5])**2 + (main[6] - nearest[6])**2 + (main[7] - nearest[7])**2 + (main[8] - nearest[8])**2 + (main[9] - nearest[9])**2 + (main[10] - nearest[10])**2 + (main[11] - nearest[11])**2 + (main[12] - nearest[12])**2 + (main[13] - nearest[13])**2 + (main[14] - nearest[14])**2 + (main[15] - nearest[15])**2 + (main[16] - nearest[16])**2 + (main[17] - nearest[17])**2 + (main[18] - nearest[18])**2 + (main[19] - nearest[19])**2 + (main[20] - nearest[20])**2 + (main[21] - nearest[21])**2 + (main[22] - nearest[22])**2)
    return dist