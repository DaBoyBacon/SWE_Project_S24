from InvalidListException import InvalidListException


# Ticket 12
class ComparePlayerToGame:
    def __init__(self):
        pass
    # Side formula: Used only in the main formula
    # Input: Two lists of ints or floats
    # Output: New list with listB[0] as newList[0] and the positive distance as newList[1]
    # Can Assume listA size == listB size
    def distanceTwoLists(listA, listB):
        print("Starting distanceTwoLists\n")

        returnList = []
        returnList.insert(0, listB[0])
        print("Example return list created " + str(returnList) + "\n")


        sum = 0.0
        print("sum = 0\n")
        for i in range(1, len(listA)):
            print("Accessing " + str(listA) + " and " + str(listB) + "\n")
            sum += pow((listA[i]-listB[i]), 2)
            
        
        num = pow(sum, 0.5)
        returnList.insert(1, num)

        return returnList
    
    def compareMergeSort(listToSort: list, listToSortSize: int):
        print("Beginning compareMergeSort")
        listClone = listToSort.copy()
        print("listClone created")
        leftList = []
        print("leftList created")
        halfPoint = listToSortSize / 2
        halfPoint += 1
        print("halfPoint created")
        leftRange = range(0, halfPoint, 1)
        print("created leftRange")
        for tracker in leftRange:
            print("tracker for loop time number ")
            print(tracker)
            leftList.insert(tracker, listClone[tracker].copy())
            print("inserted " + str(listClone[tracker]) + " to leftList\n")
        rightList = []
        for j in range(listToSortSize/2 + 1, listToSortSize):
            rightList.insert(0, listClone[j].copy())
        
        leftListNew = ComparePlayerToGame.compareMergeSort(leftList, len(leftList))
        rightListNew = ComparePlayerToGame.compareMergeSort(rightList, len(rightList))

        outputList = []
        leftTracker = 0
        rightTracker = 0
        for i in range(0, listToSortSize):
            if(leftTracker == len(leftListNew)):
                outputList.append(rightListNew[rightTracker])
                rightTracker += 1
            elif(rightTracker == len(rightListNew)):
                outputList.append(leftListNew)
                leftTracker += 1
            else:
                if(leftListNew[leftTracker][1] <= rightListNew[rightTracker][1]):
                    outputList.append(leftListNew[leftTracker])
                    leftTracker += 1
                else:
                    outputList.append(rightListNew[rightTracker])
                    rightTracker += 1
        return outputList
    


    # Main formula: Used outside of this class
    # Input: 
    # - List of lists, List[0] being the player, and every other list being a game list
    # - int of size of EVERY list in enterList
    # Output: List of which games are closest to player
    # Fails if:
    # - all lists within enterList aren't the same registered size
    # - any idx in enterList isn't a list

    def comparePlayerToGame(self, enterList: list, listSizes: int):

        print("Start ComparePlayerToGame \n")
        shouldBeListSize = int
        shouldBeListSize = len(enterList[0])
        finalListSize = shouldBeListSize - 1
        for testList in enterList:
            if (isinstance(testList, list) == False):
                print("Invalid Entry: Not a list\n")
                raise InvalidListException("Invalid Entry: Not a list\n")
            if (len(testList) != shouldBeListSize):
                print("Invalid Entry: List is too small\n")
                raise InvalidListException("Invalid Entry: List is too small\n")
            
            for i in range(1, len(testList)):
                if(isinstance(testList[i], int) == False and isinstance(testList[i], float) == False):
                    print("Invalid Entry: One of the values is NaN\n")
                    raise InvalidListException("Invalid Entry: One of the values is NaN\n")
        


        print("All lists confirmed\n")
        print("Judging distances\n")

        playerList = enterList[0]

        
        listClone = enterList.copy()
        print("enterList copied\n")
        print(listClone)
        listClone.remove(listClone[0])
        print("clone of player removed\n")
        print(listClone)
        print("\n")

        outputList = []
        print("outputList created\n")
        print(outputList)
        print("Now judging")

        for i in range(len(enterList) - 1):
            print("Judging list " + str(listClone[i]))
            appendThis = ComparePlayerToGame.distanceTwoLists(playerList, listClone[i])
            print("Created " + str(appendThis))
            outputList.append(appendThis)
            print("Output List is now " + str(outputList) + "\n")

        



        
        # Check all values to make sure they're correct
        # Check distances between said list and PlayerList using Distance Formula, and add them to a list
        outputListSize = len(outputList)
        outputList = ComparePlayerToGame.compareMergeSort(outputList, outputListSize)
        # Sort masterlist by list[x][1]
        # return masterlist
        for checkList in outputList:
            print(checkList[0])
        
        return outputList
