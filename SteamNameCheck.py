global SteamNameCheck

'''
    # makes sure an inputted username is within the API limits
    # UN must be over a character, and up to 32 characters
    
    input: string form of username
    output: True or False, whether the name follows the API conventions
'''
def SteamNameCheck(userName):
    #if name out of bounds, ret false
    if (len(userName) > 32 or len(userName) < 2):
        return False
    #otherwise, UN must be inside bounds; ret true
    else:
        return True
    