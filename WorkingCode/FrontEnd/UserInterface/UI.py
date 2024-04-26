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

ALEXSTEAMID = 76561198085073544
JOSHSTEAMID = 76561198872311178
#ANDREW'S STM ID: idk yet
SUPER_CONFIDENTIAL_API_KEY_THAT_WE_TOTALLY_DONT_WANT_STOLEN = "A65EA697948898E80E7B28E696A9DB05"

MW = tk.Tk() #instance a window
MW.title("GameWrecks") #change window title

loginFrame = tk.Frame(MW)
loginFrame.pack()
gamesFrame = tk.Frame(MW)
gamesFrame.pack_forget()

loginList = []
gamesList = []

UserAPIGames = []

def populateGames(lst):
    global gamesList
    for num in range(0,len(lst)):
        txt = lst[num]['name']
        w = tk.Message(text=txt)
        gamesList.append(w)

def runButton():
    global loginList, gamesList, loginFrame, gamesFrame, JOSHSTEAMID, ALEXSTEAMID
    
    UserName = loginList[1].get()
    
    #local debug
    print(f"Run UN called:{UserName}")
    
    retLst = PullPlayersTopGames.pullPlayersTopGames(SUPER_CONFIDENTIAL_API_KEY_THAT_WE_TOTALLY_DONT_WANT_STOLEN, JOSHSTEAMID)

    if retLst == None:
        setToLogin()
    else:
        print("HOLY SHIT IT WORKED")
        print(retLst)
        #make login widgets invis
        loginFrame.pack_forget()
    
        populateGames(retLst)
    
        for w in gamesList:
            w.master = gamesFrame
        
        for a in range(0,len(gamesList)):
            gamesList[a].grid(row=int(a/5), column= a%5)
            gamesList[a].text = retLst[a]['name']

        #Show games frame
        gamesFrame.grid()
    
def setToLogin():
    global gamesFrame, loginFrame, loginList
    
    gamesFrame.pack_forget()  #make games invis

    if(len(loginList) == 0):
        #create widgets
        InptUNLbl = tk.Label(loginFrame, text="Put in your Steam UN")              #Text to inform user to inpt name
        InptUNInp = tk.Entry(loginFrame)                                           #Text field for user to enter data
        InptUNBtn = tk.Button(loginFrame, text="Run", width=25, command=runButton) #Button to "run" username
    
        #setup order
        InptUNLbl.grid(row=0)
        InptUNInp.grid(row=1)
        InptUNBtn.grid(row=2)

        #Add their references to a list
        loginList.append(InptUNLbl)
        loginList.append(InptUNInp)
        loginList.append(InptUNBtn)

    #Make sure to "re-show" the login page
    loginFrame.pack()

setToLogin()

MW.mainloop()