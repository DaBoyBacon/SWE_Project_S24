#just to navigate back to test unit's directory
import sys
#Add our folders to path
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


MW = tk.Tk() #instance a window
MW.title("GameWrecks") #change window title

loginFrame = tk.Frame(MW)
gamesFrame = tk.Frame(MW)
suggestFrame = tk.Frame(MW)

loginWList = []
gamesWList = []
suggestWList =[]

UserAPIGames = []
SuggestedGames = []

def populateSuggestions(SuggestGamesList):
    global SuggestedGames, suggestWList, suggestFrame
    suggestWList = suggestWList[:3]
    for game in SuggestGamesList:
        txt = game[0]
        w = tk.Label(suggestFrame, text=txt, borderwidth=1, relief="solid")
        SuggestedGames.append(txt)
        suggestWList.append(w)

def showRelated():
    global MW, gamesFrame, gamesWList, UserAPIGames, SuggestedGames


    #im shitting my pants ◐ ﹏ ◐
    #Hide gamesFrame
    
    gamesFrame.grid_forget()
    
    #for i in range(0,len(gamesWList)):
    #    gamesWList[i].grid_forget()
    #gamesWList.clear()
    #Take list of games, turn it into list of lists: [[name,openWorld,combat,animation]].

    #print("UserAPIGames: " , UserAPIGames)
    gamesWithScores = MatchGamesToScores.MatchGamesToScores(sys.path[0]+"\\gamewrecks database.csv", UserAPIGames)

    print("Games with scores: ", gamesWithScores)

    openWorld = 0 #ACs for categories; will be averaged
    combat = 0
    animation = 0
    #for each category
    for cat in range(0,3):
        #for each game that we chose to consider
        for gameScore in gamesWithScores:
            val = gameScore[1+cat] #val is the game's score for the current category
            if cat==0:
                openWorld+=val
            elif cat==1:
                combat+=val
            else:
                animation+=val
                
    #print(f"Totals | OW: {openWorld} | Cmb: {combat} | Anm: {animation}")

    openWorld/=len(gamesWithScores)
    combat/=len(gamesWithScores)
    animation/=len(gamesWithScores)
    
    print(f"Totals Avg | OW: {openWorld} | Cmb: {combat} | Anm: {animation}")
    
    #Call func that takes avgs and pairs them to Suggested games


    


    
    #Call func that takes Suggestion List and make shell for frame

    if (len(suggestWList) <= 3):
        suggestWList.append(tk.Spinbox(suggestFrame, from_=3, to=15))
        suggestWList.append(tk.Button(suggestFrame, text="Re-Suggest", command=showRelated))
        suggestWList.append(tk.Button(suggestFrame, text="Re-Consider", command=fetchGames))
        
        
    totalList = AlexCompare.getDatabase([int(openWorld), int(combat), int(animation)], sys.path[0]+"\\gamewrecks database.csv", int(suggestWList[0].get()))

    print("Final List:", totalList)
    

    #Fill frame with Suggested Game names
    populateSuggestions(totalList)
    #print("children of SuggestFrame: ",suggestFrame.children)
    
    suggestWList[0].grid(row=0)
    suggestWList[1].grid(row=1)
    suggestWList[2].grid(row=2)
    
    for wInc in range(0, len(suggestWList)-3):
        suggestWList[wInc+3].grid(row=int(wInc/5), column=(wInc%5)+1)

    #re-pack
    suggestFrame.pack()
    
def populateGames(lst):
    global gamesWList, gamesFrame
    gamesWList = gamesWList[:4]
    for num in range(0,len(lst)):
        txt = lst[num]['name']
        w = tk.Label(gamesFrame, text=txt, borderwidth=1, relief="solid")
        gamesWList.append(w)

def fetchGames():
    global loginWList, gamesWList, loginFrame, gamesFrame, JOSHSTEAMID, ALEXSTEAMID, UserAPIGames, suggestFrame
    
    
    if(len(gamesWList)<4):
        gamesWList.clear()
        gamesWList.append(tk.Spinbox(gamesFrame,from_=5, to=100))
        gamesWList.append(tk.Button(gamesFrame, text="Re-Consider", command=fetchGames))
        gamesWList.append(tk.Button(gamesFrame, text="Run", command=showRelated))
        gamesWList.append(tk.Button(gamesFrame, text="Back", command=setToLogin))

    UserName = loginWList[1].get()
    
    #local debug
    print(f"Run UN called:{UserName}")
    
    retLst = PullPlayersTopGames.pullPlayersTopGames("A65EA697948898E80E7B28E696A9DB05", UserName, int(gamesWList[0].get()))

    if retLst == None:
        setToLogin()
    else:
        loginFrame.grid_forget()
        suggestFrame.grid_forget()
        #un-pack login frame or suggest frame

        UserAPIGames.clear()
        for d in retLst:
            UserAPIGames.append(d['name'])
        #Clear API list, and add list of games

        #print("HOLY SHIT IT WORKED")
        #print(retLst)
        #make login widgets invis
    
        #Create ur widgets
        populateGames(retLst)
        
        #Set all game MSGs to frame
        for w in gamesWList:
            w.master = gamesFrame
        
        #grid pack the arrows and btn
        for i in range(0, len(gamesWList) - len(retLst)):
            gamesWList[i].grid(row=i, column = 0)
        
        #grid pack MSGs
        #if len(gamesWList) != len(retLst): 
            #print("AAAAHHHHHH")
            #print(f"GL: {len(gamesWList)} | RL: {len(retLst)}")
        for a in range(0,len(retLst)):
            gamesWList[a+len(gamesWList) - len(retLst)].grid(row=int(a/5), column= a%5+1)
        

        #Show games frame
        try:
            gamesFrame.grid()
        except :
            gamesFrame.pack()
    
def setToLogin():
    global gamesFrame, loginFrame, loginWList
    gamesFrame.grid_forget()
    
    #gamesFrame.pack_forget()  #make games invis
    

    if(len(loginWList) == 0):
        #create widgets
        InptUNLbl = tk.Label(loginFrame, text="Put in your Steam ID; from the steam app, click on your profile in the top right. click \"account details\". in the top left, under your username, is your \"Steam ID\"")              #Text to inform user to inpt name
        InptUNInp = tk.Entry(loginFrame)                                           #Text field for user to enter data
        InptUNBtn = tk.Button(loginFrame, text="Run", width=25, command=fetchGames) #Button to "run" username
    
        #setup order
        InptUNLbl.grid(row=0)
        InptUNInp.grid(row=1)
        InptUNBtn.grid(row=2)

        #Add their references to a list
        loginWList.append(InptUNLbl)
        loginWList.append(InptUNInp)
        loginWList.append(InptUNBtn)

    #Make sure to "re-show" the login page
    try:
        loginFrame.grid()
    except:
        loginFrame.pack()

setToLogin()

MW.mainloop()