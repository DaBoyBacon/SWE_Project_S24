# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def testComparePlayerToGame():
    # Initialize three games, game1 being lowest bounds, game2 being avg case, and game3 being upper bounds.
    # Between Game1 and Game3, Game1 should be chosen first
    game1 = ["Game1", 1, 1, 2]
    game2 = ["Game2", 5, 5, 5]
    game3 = ["Game3", 9, 9, 9]

    print("Average Case: 4 4 4\n")
    print("Should Be: Game2, Game1, Game3")
    playerList = ["Player", 5, 5, 5]
    enterList = [playerList, game1, game2, game3]
    try:
        returnList = ComparePlayerToGame(enterList)
    except:
        print("Error has occurred. AvgCaseFail")
    else:
        if(returnList[0][0] is "Game2" and returnList[1][0] is "Game1" and returnList[2][0] is "Game3"):
            print("Average Case test passed.\n")
        else:
            print("Average Case test failed. Check algorithms. \n")

    print("\n \n")

    print("Error Case: Empty playerList\n")
    playerList = ["Player"]
    enterList = [playerList, game1, game2, game3]
    try:
        returnList = ComparePlayerToGame(enterList)
    except InvalidListException:
        print("Error Case Test passed\n")
    except:
        print("Alternative error has occurred. Check Error Throwing Code.\n")
    else:
        print("That shouldn't have worked. Check Error Throwing Code.\n")

    print("\n \n")


    print("Lowest case: PlayerList = 1, 1, 1 \n")
    playerList = ["Player", 1, 1, 1]
    enterList = [playerList, game1, game2, game3]
    try:
        returnList = ComparePlayerToGame(enterList)
    except:
        print("Error has occured. Check Code.")
    else:
        if(returnList[0][0] is "Game1" and returnList[1][0] is "Game2" and returnList[2][0] is "Game3"):
            print("LowestCase test passed\n")
        else:
            print("LowestCase test failed. Check algorithm \n")

    print("\n \n")

    print("Highest case: PlayerList = 9, 9, 9 \n")
    playerList = ["Player", 9, 9, 9]
    enterList = [playerList, game1, game2, game3]
    try:
        returnList = ComparePlayerToGame(enterList)
    except:
        print("Error has occured. Check Code.")
    else:
        if(returnList[0][0] is "Game3" and returnList[1][0] is "Game2" and returnList[2][0] is "Game1"):
            print("Highest case passed\n")
        else:
            print("Highest case error. Check algorithm")

    print("\n \n")
    print("TESTS COMPLETED. VIEW RESULTS AND CLEAN AS NEEDED")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testComparePlayerToGame()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
