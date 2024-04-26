# GetSteamPlayerInfo.py
import requests  # This line imports the 'requests' library which is used for making HTTP requests in Python. If you are getting errors here you need to
# install the requests library.

global getOwnedGames

# Define a function named 'getOwnedGames' which takes two parameters: 'apiKey' and 'steamId'. We need to figure a good way to input these from GUI.
def getOwnedGames(apiKey, steamId):
    # This is the URL to Steam's GetOwnedGames API which returns a list of games owned by a specific user. Different URL's will return different info.
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    
    # Parameters to be sent with the HTTP request to specify the API key, user's Steam ID, and additional options.
    params = {
        'key': apiKey,  # The Steam Web API key.
        'steamid': steamId,  # The Steam ID of the user whose game list you want to retrieve.
        'include_appinfo': True,  # Option to include the name and other details of each game.
        'include_played_free_games': True  # Include games that are free and have been played at least once.
    }
    
    # The 'try' block contains code that might throw an exception (error). If an error occurs, the 'except' block is executed.
    try:
        # Make a GET request to the Steam API with the specified URL and parameters.
        response = requests.get(url, params=params)
        # If the response was successful, no Exception will be raised.
        response.raise_for_status()
        # Convert the JSON response to a Python dictionary.
        data = response.json()
        # Retrieve the list of games from the response data. Default to an empty list if 'games' key is not found.
        games = data['response'].get('games', [])
        
        #print(games) #Alex debugging, don't worry

        # Create and return a list of dictionaries where each dictionary contains the name and total playtime of each game.
        return [{'name': game['name'], 'playtime_forever': game['playtime_forever']} for game in games]
    # This block handles any exceptions that occur during the HTTP request.
    except requests.exceptions.RequestException as e:
        # Print an error message if the HTTP request failed.
        print(f"Request failed: {e}")
        # Return None if an error occurs to indicate the failure of the API request.
        return None
