

global SteamNameCheck


def SteamNameCheck(userName):
    if (len(userName) > 32 or len(userName) < 2):
        return False
    else:
        return True
    