import tkinter as tk
MW = tk.Tk() #instance a window
MW.title("GameWrecks") #change window title

loginFrame = tk.Frame(MW)
loginFrame.pack()
gamesFrame = tk.Frame(MW)
gamesFrame.pack_forget()

loginList = []
gamesList = []

def populateGames():
    global gamesList
    for num in range(1,10+1):
        txt = "Game" + str(num)
        w = tk.Message(text=txt)
        gamesList.append(w)

def runButton():
    global loginList, gamesList, loginFrame, gamesFrame
    
    UserName = loginList[1].get()
    
    #local debug
    print(f"Run UN called:{UserName}")
    
    

    #make login widgets invis
    loginFrame.pack_forget()
    
    populateGames()
    
    for w in gamesList:
        w.master = gamesFrame
        
    for a in range(0,len(gamesList)):
        gamesList[a].grid(row=int(a/5), column= a%5)

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