import GetSteamPlayerInfo

global pullPlayersTopGames

def pullPlayersTopGames(apiKey, steamId):
    
    games_info = GetSteamPlayerInfo.getOwnedGames(apiKey, steamId) # Retrieve game information for the specified Steam ID using the provided API key

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