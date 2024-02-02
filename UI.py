import tkinter as tk

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text = "Your Message", font=('Arial', 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 5, font=('Arial', 16))
        self.textbox.pack(padx = 10, pady=10)

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16))
        
                
        self.root.mainloop()