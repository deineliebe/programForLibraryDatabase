import tkinter
from tkinter import ttk
import SQLQueries
import welcomeMenu

def logout(window):
    window.destroy()
    welcomeMenu.mainMenu()

def librarianFunctions(cur, conn):
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("240x300")
    welcomeLabel = ttk.Label(text="Choose action")
    welcomeLabel.grid(column=0, row=0)
    btn1 = ttk.Button(window, text="Get reader's books", command=lambda: SQLQueries.selectBooksReadersOutByReader(cur, 1))
    btn1.grid(column=0, row=1)
    btn2 = ttk.Button(window, text="Get names of author's books", command=lambda: SQLQueries.selectBooksbyAuthor(cur))
    btn2.grid(column=0, row=2)
    btn3 = ttk.Button(window, text="Get cipher of book by it's name", command=lambda: SQLQueries.selectBooksbyName(cur))
    btn3.grid(column=0, row=3)
    btn4 = ttk.Button(window, text="Get book's date of attachment to the reader", command=lambda: SQLQueries.selectBooksReadersOutByReader(cur, 2))
    btn4.grid(column=0, row=4)
    btn5 = ttk.Button(window, text="Get number of readers", command=lambda: SQLQueries.countOfUsers(cur))
    btn5.grid(column=0, row=5)
    btn6 = ttk.Button(window, text="Add new reader", command=lambda: SQLQueries.addReader(cur, conn))
    btn6.grid(column=0, row=6)
    btn7 = ttk.Button(window, text="Delete book", command=lambda: SQLQueries.deleteBook(cur, conn))
    btn7.grid(column=0, row=7)
    btn8 = ttk.Button(window, text="Change book's cypher", command=lambda: SQLQueries.updateBookCypher(cur, conn))
    btn8.grid(column=0, row=8)
    btn9 = ttk.Button(window, text="Get reference", command=lambda: SQLQueries.reference(cur))
    btn9.grid(column=0, row=9)
    btn10 = ttk.Button(window, text="Get report", command=lambda: SQLQueries.report(cur))
    btn10.grid(column=0, row=10)
    btn11 = ttk.Button(window, text="Logout", command=lambda: logout(window))
    btn11.grid(column=0, row=11)
    window.mainloop()