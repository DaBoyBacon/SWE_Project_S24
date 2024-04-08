import requests # Start with importing requests library to make HTTP requests to use the Steam API

def getSteamPlayerInfo(apiKey, steamIds): # The getSteamPlayerInfo takes two parameters, the API key and the steam IDs

    # Convert list of Steam IDs to the correct format
    if isinstance(steamIds, list): # Is instance function checks if steamIds is a list
        steamIds = ','.join(steamIds) # If it is a list it joins the Steam IDs into a comma-separated string because the Steam API expects the Steam IDs to be passed as such.

    # Construct the request URL
    url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/" # Have to combine the base URL with the requested parameters key and steamIds
    params = { # Creates a dictionary called params to store the query parameters
        'key': apiKey,
        'steamids': steamIds
    }

    # Makes a GET request to the constructed URL
    response = requests.get(url, params=params)

    # After the request it checks for the status code response. 200 is a successful request. Anything else is an error
    if response.status_code == 200:
        data = response.json()
        return data['response']['players'] # Returns dictionary containing player info if successful
    else:
        print(f"Error fetching player information: {response.status_code}")
        return None # Returns None if unsuccessful

# Example usage
api_key = 'A65EA697948898E80E7B28E696A9DB05' #GameWrecks API key
steam_ids = ['76561198039845746']  # My steam ID
player_info = getSteamPlayerInfo(api_key, steam_ids)
print(player_info) # Upon successful request the function extracts the JSON data from the response and returns the players key from the response dictionary which contains the players information
