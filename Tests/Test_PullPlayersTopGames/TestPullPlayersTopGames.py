import unittest

# Import the function you want to test
from your_module import pullPlayersTopGames

class TestPullPlayersTopGames(unittest.TestCase):
    # Define a test method that starts with "test_"
    def test_pull_players_top_games(self):
        # Define inputs
        steam_user_id = "inputted_id"
        
        # Call the function
        result = pullPlayersTopGames(steam_user_id)
        
        # Define expected output
        expected_output = ["Game 1", "Game 2", "Game 3", "Game 4", "Game 5"]
        
        # Assert that the result matches the expected output
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
