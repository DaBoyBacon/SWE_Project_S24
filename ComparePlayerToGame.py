from InvalidListException import InvalidListException


# Ticket 12
class ComparePlayerToGame:

    # Side formula: Used only in the main formula
    # Input: Two lists of ints or floats
    # Output: New list with listB[0] as newList[0] and the positive distance as newList[1]
    # Can Assume listA size == listB size
    def distanceTwoLists(listA, listB):
        returnList = [listB[0], 0]


        sum = 0
        for i in range(1, listA.__sizeof__ + 1):
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

    def comparePlayerToGame(enterList: list, listSizes: int) -> list:

        print("Start ComparePlayerToGame \n")
        shouldBeListSize = 4
        for testList in enterList:
            if (isinstance(testList, list) == False):
                raise InvalidListException("Invalid Entry: Not a list\n")
            if (len(testList) != listSizes):
                raise InvalidListException("Invalid Entry: List is too small\n")
            
            for i in range(1, testList.__sizeof__ + 1):
                if(isinstance(testList[i], int) == False and isinstance(testList[i], float) == False):
                    raise InvalidListException("Invalid Entry: One of the values is NaN")
        


        print("All lists confirmed\n")
        print("Judging distances\n")

        playerList = enterList[0]
        playerFirstScore = playerList[1]
        playerSecondScore = playerList[2]
        playerThirdScore = playerList[3]

        # For list in enterlist[1] to enterlist[end]
        clone = enterList.copy()
        clone.remove(enterList[0])

        return clone
        # Check all values to make sure they're correct
        # Check distances between said list and PlayerList using Distance Formula, and add them to a list

        # Sort masterlist by list[x][1]
        # return masterlist