from InvalidListException import InvalidListException

class ComparePlayerToGame:

    def comparePlayerToGame(enterList):

        print("Start ComparePlayerToGame \n")
        shouldBeListSize = 4
        for testList in enterList:
            if not isinstance(testList, list):
                raise InvalidListException("Invalid Entry: Not a list\n")
            if (len(testList) != 4):
                raise InvalidListException("Invalid List: Not correct size\n")

        print("All lists confirmed\n")
        print("Judging distances")

        playerList = enterList[0]
        playerFirstScore = playerList[1]
        playerSecondScore = playerList[2]
        playerThirdScore = playerList[3]




        for i in range(1, len(enterList)):
            print("e")