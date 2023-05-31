import tkinter
from tkinter import ttk
import SQLQueries
import welcomeMenu

def logout(window):
    window.destroy()
    welcomeMenu.mainMenu()

def returnToAdminMenu(window, cur, conn):
    window.destroy()
    adminFunctions(cur, conn)

def adminreadersFunctions(previousWindow, cur, conn):
    previousWindow.destroy()
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("122x145")
    welcomeLabel = ttk.Label(text="Choose an action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Get info about reader", command=lambda: SQLQueries.selectAllReaders(cur))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Add reader", command=lambda: SQLQueries.addReader(cur, conn))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Update reader's info", command=lambda: SQLQueries.updateReaders(cur, conn))
    btn3.grid(column=0, row=3)
    btn4 = ttk.Button(window, text="Delete reader", command=lambda: SQLQueries.deleteReader(cur, conn))
    btn4.grid(column=0, row=4)
    btn6 = ttk.Button(window, text="Return", command=lambda: returnToAdminMenu(window, cur, conn))
    btn6.grid(column=0, row=6)
    window.mainloop()

def adminHallsFunctions(previousWindow, cur, conn):
    previousWindow.destroy()
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("122x145")
    welcomeLabel = ttk.Label(text="Choose an action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Get info about hall", command=lambda: SQLQueries.selectAllHalls(cur))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Add hall", command=lambda: SQLQueries.addHall(cur, conn))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Update hall's info", command=lambda: SQLQueries.updateHall(cur, conn))
    btn3.grid(column=0, row=3)
    btn4 = ttk.Button(window, text="Delete hall", command=lambda: SQLQueries.deleteHall(cur, conn))
    btn4.grid(column=0, row=4)
    btn6 = ttk.Button(window, text="Return", command=lambda: returnToAdminMenu(window, cur, conn))
    btn6.grid(column=0, row=6)
    window.mainloop()

def adminBooksFunctions(previousWindow, cur, conn):
    previousWindow.destroy()
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("122x145")
    welcomeLabel = ttk.Label(text="Choose an action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Get info about book", command=lambda: SQLQueries.selectAllBooks(cur))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Add book", command=lambda: SQLQueries.addBook(cur, conn))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Update book's info", command=lambda: SQLQueries.updateBook(cur, conn))
    btn3.grid(column=0, row=3)
    btn4 = ttk.Button(window, text="Delete book", command=lambda: SQLQueries.deleteBook(cur, conn))
    btn4.grid(column=0, row=4)
    btn6 = ttk.Button(window, text="Return", command=lambda: returnToAdminMenu(window, cur, conn))
    btn6.grid(column=0, row=6)
    window.mainloop()

def adminOtherFunctions(previousWindow, cur, conn):
    previousWindow.destroy()
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("135x100")
    welcomeLabel = ttk.Label(text="Choose an action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Reader get a book", command=lambda: SQLQueries.readerGetABook(cur, conn))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Reader returned a book", command=lambda: SQLQueries.deleteRecord(cur, conn))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Return", command=lambda: returnToAdminMenu(window, cur, conn))
    btn3.grid(column=0, row=3)
    window.mainloop()

def adminFunctions(cur, conn):
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("220x150")
    welcomeLabel = ttk.Label(text="Choose an object you need to interact to")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Readers", command=lambda: adminreadersFunctions(window, cur, conn))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Halls", command=lambda: adminHallsFunctions(window, cur, conn))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Books", command=lambda: adminBooksFunctions(window, cur, conn))
    btn3.grid(column=0, row=3)
    btn4 = ttk.Button(window, text="Other", command=lambda: adminOtherFunctions(window, cur, conn))
    btn4.grid(column=0, row=4)
    btn5 = ttk.Button(window, text="Logout", command=lambda: logout(window))
    btn5.grid(column=0, row=5)
    window.mainloop()