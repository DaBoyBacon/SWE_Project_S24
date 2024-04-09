def pullPlayersTopGames(apiKey, steamIds):
    player_info = getSteamPlayerInfo(apiKey, steamIds)
    
    if player_info:
        # Assuming the top 5 most played games are found in 'game_count' field of each player info
        # Extracting top 5 games from player info
        top_games = []
        for player in player_info:
            top_games.extend(player.get('game_count', []))
        
        # Sorting the games based on their play counts
        top_games.sort(reverse=True)
        
        return top_games[:5]  # Returning top 5 most played games
    else:
        return None
