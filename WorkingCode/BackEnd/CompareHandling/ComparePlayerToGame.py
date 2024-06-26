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
        returnList = [listB[0], 0]


        sum = 0
        for i in range(1, listA.__sizeof__):
            sum += (listA[i]-listB[i])^2
            
        
        num = sum^1/2
        returnList[1] = num

        return returnList

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
        shouldBeListSize = enterList[0].__sizeof__
        finalListSize = shouldBeListSize - 1
        for testList in enterList:
            if (isinstance(testList, list) == False):
                raise InvalidListException("Invalid Entry: Not a list\n")
            if (len(testList) != shouldBeListSize):
                raise InvalidListException("Invalid Entry: List is too small\n")
            
            for i in range(1, testList.__sizeof__):
                if(isinstance(testList[i], int) == False and isinstance(testList[i], float) == False):
                    raise InvalidListException("Invalid Entry: One of the values is NaN")
        


        print("All lists confirmed\n")
        print("Judging distances\n")

        playerList = enterList[0]
        playerFirstScore = playerList[1]
        playerSecondScore = playerList[2]
        playerThirdScore = playerList[3]

        
        clone = enterList.copy()
        clone.remove(enterList[0])

        outputList = []


        for listFromClone in clone:
            addThisList = ComparePlayerToGame.distanceTwoLists(playerList, listFromClone)
            outputList.append(addThisList)

        



        
        # Check all values to make sure they're correct
        # Check distances between said list and PlayerList using Distance Formula, and add them to a list

        # Sort masterlist by list[x][1]
        # return masterlist
        return outputList
