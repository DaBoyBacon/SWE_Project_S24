#just to navigate back to test unit's directory
import sys


#Add our folders to path
#print(sys.path)
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\PlayerSteamHandling")
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\GameSteamHandling")
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\CompareHandling")
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

gamesFrame = tk.Frame(MW)
gamesWidgets = []

UserAPIGames = []

suggestFrame = tk.Frame(MW)
suggestWidgets = []

#returns list of strings
def getGameNames(UN: str, numOfGames=5):
    #print(f"getGameNames.UN: {UN}")
    retDict = PullPlayersTopGames.pullPlayersTopGames("A65EA697948898E80E7B28E696A9DB05", UN, numOfGames) #Get user's top 5 games
    #print("return from pullPlayerTopGames", retDict)
    gameList = []
    if (retDict != None):
        for d in retDict:
            gameList.append(d['name'])
            
    return gameList

def getAvg(inptList):
    openWorld = 0 #ACs for categories; will be averaged
    combat = 0
    animation = 0
    #for each category
    for cat in range(0,3):
        #for each game that we chose to consider
        for gameScore in inptList:
            val = gameScore[1+cat] #val is the game's score for the current category
            if cat==0:
                openWorld+=val
            elif cat==1:
                combat+=val
            else:
                animation+=val
                
    #print(f"Totals | OW: {openWorld} | Cmb: {combat} | Anm: {animation}")

    openWorld/=len(inptList)
    combat/=len(inptList)
    animation/=len(inptList)
    
    return [int(openWorld), int(combat), int(animation)]

def populateSuggest(listOfGames):
    global suggestFrame, suggestWidgets
    print("Populate Suggest")
    for name in listOfGames:
        Lbl = tk.Label(suggestFrame, text = name, borderwidth=1, relief="solid")
        suggestWidgets.append(Lbl)
        
    #grid populated suggestions
    for wInc in range(0,len(listOfGames)):
        suggestWidgets[wInc+3].grid(row=int(wInc/5),column=(wInc%5)+1)

def refreshSuggest():
    global suggestFrame, suggestWidgets
    print("Run refreshSuggest")
    
    csvFilepath = sys.path[0]+"\\gamewrecks database.csv"
    NewFrame = GamesFrame.getGameFrame(MW, refreshSuggest, clearSuggest, 3, 15)
    suggestFrame.grid_remove()
    suggestFrame = NewFrame[0]
    
    gamesWithScores = MatchGamesToScores.MatchGamesToScores(csvFilepath, UserAPIGames)
    #gives us a listof [["game",a,b,c],["game2",a,b,c],...]

    #gives avg of a, b, and c
    avg = getAvg(gamesWithScores)
    
    #matches to n games
    FinalList = AlexCompare.getDatabase(avg, csvFilepath, int(suggestWidgets[0].get()))
    
    #set new sugg widgets
    suggestWidgets = NewFrame[1]
    
    print(f"FinalList: {FinalList}")
    
    #populate widgets w FinalList
    populateSuggest(FinalList)
    
        
    MW.grid()
    
def clearSuggest():
    global MW, suggestFrame, suggestWidgets
    print("Run clearSuggest")
    suggestFrame.grid_remove()
    suggestFrame = tk.Frame(MW)
    suggestWidgets.clear()
    MW.grid()

def showSuggestions():
    global suggestFrame, suggestWidgets, MW
    print("show Sugg")
    csvFilepath = sys.path[0]+"\\gamewrecks database.csv"
    NewFrame = GamesFrame.getGameFrame(MW, refreshSuggest, clearSuggest, 3, 15)
    
    suggestFrame = NewFrame[0]
    suggestWidgets = NewFrame[1]
    
    gamesWithScores = MatchGamesToScores.MatchGamesToScores(csvFilepath, UserAPIGames)
    #gives us a listof [["game",a,b,c],["game2",a,b,c],...]
    avg = getAvg(gamesWithScores)
    
    FinalList = AlexCompare.getDatabase(avg, csvFilepath)
    print(f"FinalList: {FinalList}")
    
    populateSuggest(FinalList)

    
    MW.grid()
    
    

#takes UserAPIGames, turns it into gamesWidgets, and loads those into grid
def AddAPIGamesToFrame():
    global UserAPIGames, gamesFrame, gamesWidgets
    
    #print(f"widgets in addApiGamesToFrame(): {gamesWidgets}")

    for name in UserAPIGames:
        #print(f"adding widg to games: {len(gamesWidgets)}")
        Lbl = tk.Label(gamesFrame,text=name, borderwidth=1,relief="solid")
        gamesWidgets.append(Lbl)
        

    for wInc in range(0,len(UserAPIGames)):
        gamesWidgets[wInc+4].grid(row=int(wInc/5), column=(wInc%5)+1)

#change num of games shown in gamesFrame; for refresh
def refreshGames():
    global gamesFrame, UserAPIGames, gamesWidgets, username, suggestWidgets
    #print("refresh games")
    oldFrame = gamesFrame
    
    NewFrame = GamesFrame.getGameFrame(MW, refreshGames, clearGames, nextFunc=showSuggestions)
    gamesFrame = NewFrame[0]
    
    UserAPIGames = getGameNames(username, int(gamesWidgets[0].get()))
    gamesWidgets = NewFrame[1]
    AddAPIGamesToFrame()
    
    oldFrame.grid_remove()
    #print("Children leftover",oldFrame.children)
    if len(suggestWidgets) > 0:
        clearSuggest()
    
#removes the Games widget; to go back to base login
def clearGames():
    global gamesFrame, MW
    print("clear games")
    gamesFrame.grid_forget()
    gamesFrame = tk.Frame(MW)
    if len(suggestWidgets) != 0:
        clearSuggest()
    MW.grid()
    
#first load after clicking "login"
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
        
    
    

    
    
#What happens when u click login; adds a the gameFrame
def clickLogin():
    global gamesFrame, MW, loginFrame, username, gamesWidgets, suggestWidgets
    
    #load games into gamesFrame
    username = loginWidgets[1].get() 
    
    if len(getGameNames(username)) > 0:
        if(len(suggestWidgets)>0):
            clearSuggest()
        if(len(gamesWidgets)>0):
            clearGames()
        
        NewFrame = GamesFrame.getGameFrame(MW, refreshGames, clearGames, nextFunc=showSuggestions)
        gamesFrame = NewFrame[0]
        gamesWidgets = NewFrame[1].copy()
        #print(f"ClickLogin.gamesWidgets: {gamesWidgets}")
        gamesFrame.grid(row=2)
        

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