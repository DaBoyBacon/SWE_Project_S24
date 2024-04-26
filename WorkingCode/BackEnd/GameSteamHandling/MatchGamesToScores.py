# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:31:01 2024

@author: Guita
"""
import csv

def MatchGamesToScores(csv_file, input_games):
    gameScores = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:  # Read in the CSV file row by row 
            game_name = row[0].strip().lower()  # Convert name in database to lowercase and strip spaces, to prevent formatting error
            for input_game in input_games: # loop to find scores for each input game name
                if input_game.strip().lower() in game_name:  # Convert input game name to lowercase and strip spaces, compare to data base
                    intList = [int(score) for score in row[1:]] # make list of scores for selected game
                    gameScores.append([row[0]] + intList) # int score elements following game name, append whole list to gameScores
                    break  # Stop searching for this game once found
    return gameScores

# Example usage:
# game_scores = MatchGamesToScores2('games_test.csv', ["Valheim", "ELDEN RING"])
# print(game_scores)
# output: [['Valheim', 10, 8, 5], ['New World', 10, 8, 3]]
