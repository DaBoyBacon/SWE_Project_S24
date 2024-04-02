from InvalidListException import InvalidListException

class ComparePlayerToGame:

    # Side formula: Used only in the main formula
    # Input: Two lists of ints or floats
    # Output: New list with listB[0] as newList[0] and the positive distance as newList[1]
    # If listA size > listB size, create a copy of listB the same size as listA, with 0 as the extra values
    def distanceTwoLists(listA, listB):
        returnList = [listB[0], 0]

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
            if not isinstance(testList, list):
                raise InvalidListException("Invalid Entry: Not a list\n")
            if not (len(testList) == listSizes):
                raise InvalidListException("Invalid Entry: List is too small\n")

        print("All lists confirmed\n")
        print("Judging distances\n")

        playerList = enterList[0]
        playerFirstScore = playerList[1]
        playerSecondScore = playerList[2]
        playerThirdScore = playerList[3]


        # check all of the values to make sure they're all of the correct instance (int or float)

        # For list in enterlist[1] to enterlist[end]
        # Check all values to make sure they're correct
        # Check distances between said list and PlayerList using Distance Formula, and add them to a list

        # Sort masterlist by list[x][1]
        # return masterlist