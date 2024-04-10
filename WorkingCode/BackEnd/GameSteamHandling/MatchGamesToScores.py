# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:48:55 2024

@author: Guita
"""

import csv

def MatchGamesToScores(csv_file):
    gameScores = []
    x: int
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            intList = []
            for x in range(1, len(row), 1) :
                intList.append(int(row[x]))
            gameScores.append([row[0]]+ intList)
    return gameScores

# Example usage:
# game_scores = MatchGamesToScore('games_test.csv')
# print(game_scores)

