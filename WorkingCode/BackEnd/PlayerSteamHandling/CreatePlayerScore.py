def CreatePlayerScore(games):
    if not games:
        return 0

    totalScore = 0
    for game in games:
        gameName, openWorldness, combat, animation = game
        gameScore = (openWorldness + combat + animation) / 3
        totalScore += gameScore

    averageScore = totalScore / len(games)
    return averageScore