# PullPlayersTopGames.py
import sys
from GetSteamPlayerInfo import getOwnedGames  # Imports the getOwnedGames module from GetSteamPlayerinfo.py

def pullPlayersTopGames(apiKey, steamId):
    
    games_info = getOwnedGames(apiKey, steamId) # Retrieve game information for the specified Steam ID using the provided API key

    if games_info: # Checks if game info is available
        top_games = sorted(games_info, key=lambda x: x['playtime_forever'], reverse=True) # Sorts games by playtime
        top_ten_games = top_games[:10]
        print("Top 10 Played Games:")
        for game in top_ten_games: # Displays to the console formatted
            hours_played = game['playtime_forever'] / 60
            print(f"{game['name']} - {hours_played:.2f} hours")
        return top_ten_games
    else: # Error catch
        print("No games data available.")
        return None

# This block of code is merely for testing on a personal computer through the command line, does not mess with surrounding code
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python PullPlayersTopGames.py <API_KEY> <STEAM_ID>")
        sys.exit(1)
    api_key = sys.argv[1]
    steam_id = sys.argv[2]
    pullPlayersTopGames(api_key, steam_id)
