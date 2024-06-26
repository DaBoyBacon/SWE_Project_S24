#Ticket
##9
#Create Steam Name Handler

#define SteamNameCheck as a global function
global SteamNameCheck

def SteamNameCheck(userName: str) -> bool:
    """This functions returns True when the inputted userName is within the Steam API formatting

    Parameters
    ----------
    userName : str
        The Steam name of the user operating the program
    
    Returns
    -------
    boolean :
        True if userName meets API needs.
    """

    #if name out of bounds, return false
    if (len(userName) > 32 or len(userName) < 2):
        return False
    #otherwise, return true
    else:
        return True