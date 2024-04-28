import csv

global getDatabase

def getDatabase(AvgList, csv_file, numRecommend=5):
    print(f"Avg list: {AvgList} | Num Rec: {numRecommend}")
    #if list exists and is [a,b,c]
    if (AvgList!= None):
        if (len(AvgList)==3):
            #print("Passed the two ifs; getDatabase running")
            gameScores = []
            with open(csv_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:  # Read in the CSV file row by row 
                    game_name = row[0].strip().lower()  # Convert name in database to lowercase and strip spaces, to prevent formatting error
                    score = (abs(int(row[1].strip()) - AvgList[0]))  #score = diff btw Avg[a] and game[a]
                    score += (abs(int(row[2].strip()) - AvgList[1])) #score += diff btw Avg[b] and game[b]
                    score += (abs(int(row[3].strip()) - AvgList[2])) #score += diff btw Avg[b] and game[b]
                    gameScores.append([game_name, score])
                    
            #print(f"okay, judged all the games: {gameScores}")
            ItScore = 0
            returnScores = []
            while True:
                for game in gameScores:
                    if game[1] == ItScore:
                        returnScores.append(game)
                    if len(returnScores) >= numRecommend: 
                        print(f"Suggest Limit Reached: {numRecommend}")
                        return returnScores
                ItScore += 1
                if (ItScore > 15):
                    print(f"large ItScore: {ItScore}")
                    break
            return returnScores