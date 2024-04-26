#just to navigate back to test unit's directory
import sys
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\PlayerSteamHandling")
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\GameSteamHandling")
sys.path.append(sys.path[0]+"\\..\\..\\BackEnd\\CompareHandling")
print(sys.path)
#debug path
import tkinter as tk
import PullPlayersTopGames
import GetSteamPlayerInfo


MW = tk.Tk() #instance a window
MW.title("GameWrecks") #change window title

loginFrame = tk.Frame(MW)
loginFrame.pack()
gamesFrame = tk.Frame(MW)
gamesFrame.pack_forget()
suggestFrame = tk.Frame(MW)
suggestFrame.pack_forget()

loginWList = []
gamesWList = []
suggestWList =[]

UserAPIGames = []
SuggestedGames = []
def showRelated():
    global MW, gamesFrame, gamesWList, UserAPIGames, SuggestedGames
    #im shitting my pants ◐ ﹏ ◐
    #Hide gamesFrame
    gamesFrame.grid_forget()
    #for i in range(0,len(gamesWList)):
    #    gamesWList[i].grid_forget()
    #gamesWList.clear()
    #Take list of games, turn it into list of lists: [[name,openWorld,combat,cartoon]].
    scoreList = [["Minecraft", 10, 4, 7]]
    

    openWorld = 0 #ACs for categories; will be averaged
    combat = 0
    cartoon = 0
    #for each category
    for cat in range(0,3):
        #for each game that we chose to consider
        for gameScore in scoreList:
            val = gameScore[1+cat] #val is the game's score for the current category
            if cat==0:
                openWorld+=cat
            elif cat==1:
                combat+=cat
            else:
                cartoon+=cat
                
    openWorld/=len(scoreList)
    combat/=len(scoreList)
    cartoon/=len(scoreList)
        
        

    #Call func that takes avgs and pairs them to Suggested games

    #Call func that takes Suggestion List and make shell for frame

    #Fill frame with Suggested Game names

    #re-pack
    
def populateGames(lst):
    global gamesWList
    gamesWList = gamesWList[:4]
    for num in range(0,len(lst)):
        txt = lst[num]['name']
        w = tk.Message(text=txt, borderwidth=1, relief="solid")
        gamesWList.append(w)

def fetchGames():
    global loginWList, gamesWList, loginFrame, gamesFrame, JOSHSTEAMID, ALEXSTEAMID, UserAPIGames
    
    if(len(gamesWList)<4):
        gamesWList.clear()
        gamesWList.append(tk.Spinbox(gamesFrame,from_=5, to=100))
        gamesWList.append(tk.Button(gamesFrame, text="Re-Consider", command=fetchGames))
        gamesWList.append(tk.Button(gamesFrame, text="Run", command=showRelated))
        gamesWList.append(tk.Button(gamesFrame, text="Back", command=setToLogin))

    UserName = loginWList[1].get()
    
    #local debug
    print(f"Run UN called:{UserName}")
    
    retLst = PullPlayersTopGames.pullPlayersTopGames(SUPER_SECRET_KEY_THAT_SHOULDNT_BE_HARD_CODED, UserName, int(gamesWList[0].get()))

    if retLst == None:
        setToLogin()
    else:
        loginFrame.grid_forget()
        UserAPIGames.clear()
        for d in retLst:
            UserAPIGames.append(d['name'])
        #print("HOLY SHIT IT WORKED")
        #print(retLst)
        #make login widgets invis
        loginFrame.pack_forget()
    
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
        gamesFrame.grid()
    
def setToLogin():
    global gamesFrame, loginFrame, loginWList
    
    gamesFrame.pack_forget()  #make games invis
    

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
    loginFrame.grid()


setToLogin()

MW.mainloop()