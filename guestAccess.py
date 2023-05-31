import tkinter
from tkinter import ttk
import SQLQueries
import welcomeMenu

def logout(window):
    window.destroy()
    welcomeMenu.mainMenu()

def guestFunctions(cur, conn):
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("200x100")
    welcomeLabel = ttk.Label(text="Choose action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Check if there is a book in database", command=lambda: SQLQueries.selectIfBookbyName(cur))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Show information about library", command=lambda: SQLQueries.selectAllBooksInHalls(cur))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Logout", command=lambda: logout(window))
    btn3.grid(column=0, row=3)
    window.mainloop()