#just to navigate back to test unit's directory
import sys

#Add our folders to path
#print(sys.path)
sys.path.append(sys.path[0]+"\\SWE_Project_S24\\WorkingCode\\BackEnd\\PlayerSteamHandling")
sys.path.append(sys.path[0]+"\\SWE_Project_S24\\WorkingCode\\BackEnd\\GameSteamHandling")
sys.path.append(sys.path[0]+"\\SWE_Project_S24\\WorkingCode\\BackEnd\\CompareHandling")
#print(sys.path)

#debug path

import tkinter as tk
import PullPlayersTopGames
import GetSteamPlayerInfo
import MatchGamesToScores
import AlexCompare
import GamesFrame


MW = tk.Tk() #instance a window
MW.title("GameWrecks") #change window title

username = ""

loginFrame = tk.Frame(MW)
loginWidgets = []

gamesFrame : tk.Frame
gamesWidgets = []

UserAPIGames = []

#returns list of strings
def getGameNames(UN: str, numOfGames=5):
    print(f"getGameNames.UN: {UN}")
    retDict = PullPlayersTopGames.pullPlayersTopGames("A65EA697948898E80E7B28E696A9DB05", UN, numOfGames) #Get user's top 5 games
    print("return from pullPlayerTopGames", retDict)
    gameList = []
    if (retDict != None):
        for d in retDict:
            gameList.append(d['name'])
            
    return gameList


def showSuggestions():
    print("show Sugg")
    

def AddAPIGamesToFrame():
    global UserAPIGames, gamesFrame, gamesWidgets
    
    #print(f"widgets in addApiGamesToFrame(): {gamesWidgets}")

    for name in UserAPIGames:
        #print(f"adding widg to games: {len(gamesWidgets)}")
        Lbl = tk.Label(gamesFrame,text=name, borderwidth=1,relief="solid")
        gamesWidgets.append(Lbl)
        

    for wInc in range(0,len(UserAPIGames)):
        gamesWidgets[wInc+4].grid(row=int(wInc/5), column=(wInc%5)+1)

#change num of games shown in gamesFrame
def refreshGames():
    global gamesFrame, UserAPIGames, gamesWidgets, username
    #print("refresh games")
    oldFrame = gamesFrame
    
    NewFrame = GamesFrame.getGameFrame(MW, refreshGames, showSuggestions, clearGames)
    gamesFrame = NewFrame[0]
    
    UserAPIGames = getGameNames(username, int(gamesWidgets[0].get()))
    gamesWidgets = NewFrame[1]
    AddAPIGamesToFrame()
    
    oldFrame.grid_remove()
    #print("Children leftover",oldFrame.children)
    
    
    
def clearGames():
    global gamesFrame, MW
    print("clear games")
    gamesFrame.grid_forget()
    gamesFrame = tk.Frame(MW)
    

def loadGameFrame(username):
    global UserAPIGames, gamesWidgets
    #do the stuff to add games to gameFrame
    print("Loading games frame")
    
    #do api call and store into UserAPIGames
    #listOfUserGames = ["name1","name2", "name3"] #= getusergames(APIKey, UN)
    
    UserAPIGames = getGameNames(username)
    
    #print("U-API: ", UserAPIGames)
    #print(f"widgets before addApiGamesToFrame(): {gamesWidgets}")
    
    AddAPIGamesToFrame()
        
    
    

    
    

def clickLogin():
    global gamesFrame, MW, loginFrame, username, gamesWidgets
    NewFrame = GamesFrame.getGameFrame(MW, refreshGames, showSuggestions, clearGames)
    gamesFrame = NewFrame[0]
    gamesWidgets = NewFrame[1].copy()
    #print(f"ClickLogin.gamesWidgets: {gamesWidgets}")
    gamesFrame.grid(row=2)
    
    #load games into gamesFrame
    username = loginWidgets[1].get() 
    
    loadGameFrame(username)
    
    
    

def setupLoginFrame():
    global loginWidgets, loginFrame, MW
    loginWidgets.append(tk.Label(loginFrame, text="Put in your Steam ID; from the steam app, click on your profile in the top right. click \"account details\". in the top left, under your username, is your \"Steam ID\""))              #Text to inform user to inpt name
    loginWidgets.append(tk.Entry(loginFrame))                                           #Text field for user to enter data
    loginWidgets.append(tk.Button(loginFrame, text="Run", width=25, command=clickLogin)) #Button to "run" username
    
    for wInc in range(0,len(loginWidgets)):
        loginWidgets[wInc].grid(row=wInc)
    
    loginFrame.grid() #assembles login frame
    loginFrame.grid(row=0)        
    MW.grid()         #assembles main
    
setupLoginFrame()

MW.grid()

MW.mainloop()