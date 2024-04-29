from asyncio.windows_events import NULL
from re import A
import tkinter as tk

global getGameFrame

def getGameFrame(master, refrFunc, backFunc, From=5, To=100, nextFunc=None) -> list:
        gameFrame = tk.Frame(master)
        permWidgets = []
        permWidgets.append(tk.Spinbox(gameFrame,from_=From, to=To))
        permWidgets.append(tk.Button(gameFrame, text="Re-Consider", command=refrFunc))
        permWidgets.append(tk.Button(gameFrame, text="Back", command=backFunc))
        if (nextFunc != None):
            permWidgets.append(tk.Button(gameFrame, text="Run", command=nextFunc))
        for wInc in range(0, len(permWidgets)):
            permWidgets[wInc].grid(row=wInc)
            
        gameFrame.grid()
        return [gameFrame,permWidgets]