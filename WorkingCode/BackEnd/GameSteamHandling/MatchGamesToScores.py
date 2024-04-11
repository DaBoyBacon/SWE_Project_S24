# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:48:55 2024

@author: Guita
"""

import csv

def MatchGamesToScores(csv_file):
    gameScores = [] # create gameScores array that will contain our final output
    x: int
    with open(csv_file, 'r') as file:
        reader = csv.reader(file) # Read in the CSV file row by row 
        for row in reader:
            intList = []
            for x in range(1, len(row), 1) : # Create a list of int values from the score columns(not the name column because it will be a string)
                intList.append(int(row[x]))
            gameScores.append([row[0]]+ intList) # Append the int values to the string name of game, and append that whole list as an element in gameScores
    return gameScores 

# Example usage:
# game_scores = MatchGamesToScore('games_test.csv')
# print(game_scores)

