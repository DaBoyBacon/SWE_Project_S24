<<<<<<< HEAD
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
=======


global SteamNameCheck


def SteamNameCheck(userName):
    if (len(userName) > 32 or len(userName) < 2):
        return False
    else:
        return True
    
>>>>>>> 45c2ec591d3cfa11987d85df133ce5b188b794ba
