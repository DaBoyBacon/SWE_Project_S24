# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 00:08:08 2024

@author: Guita
"""

import unittest
from MatchGamesToScores import MatchGamesToScores

class TestMatchGamesToScores(unittest.TestCase):
    def testMatchGamesToScores(self):
        # Define different test cases with variable inputs
        testCases = [
            {
                'inputCsv': 'testCSVforGamewreck.csv', # must have 'testCSVforGamewreck.csv' in Working Directory
                'expectedOutput': [
                    ['Super Mario', 9, 8, 6],
                    ['Tetris', 8, 7, 8],
                    ['Zelda', 5, 4, 9]
                ]
            },
            {
                'inputCsv': 'testCSVforGamewreck2.csv', # must have 'testCSVforGamewreck2.csv' in Working Directory
                'expectedOutput': [
                    ['Just Dance', 1, 2, 3]
                ]
            },
            # Add more test cases as needed
        ]

        # Iterate through test cases and run assertions
        for testCase in testCases:
            inputCsv = testCase['inputCsv']
            expectedOutput = testCase['expectedOutput']

            result = MatchGamesToScores(inputCsv)
        # Check if expected results are equal tooutput from function
            self.assertEqual(result, expectedOutput)

if __name__ == '__main__':
    unittest.main()
