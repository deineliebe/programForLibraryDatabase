import adminAccess
import librarianAccess
import guestAccess
import tkinter
from tkinter import messagebox
from tkinter import ttk
import connection

def getGuestAccess(window):
    window.destroy()
    conn = connection.connect("guest", "qwerty")
    cur = conn.cursor()
    guestAccess.guestFunctions(cur, conn)
    cur.close()
    conn.close()

def getTxt(loginEntry, passwordEntry, window):
    login = loginEntry.get()
    password = passwordEntry.get()
    clear(loginEntry, passwordEntry)
    authorisation(login, password, window)

def authorisation(login, password, window):
    conn = connection.connect(login, password)
    if (conn):
        window.destroy()
        cur = conn.cursor()
        if (login == "guest"):
            guestAccess.guestFunctions(cur, conn)
        elif (login == "librarian"):
            librarianAccess.librarianFunctions(cur, conn)
        elif (login == "admin"):
            adminAccess.adminFunctions(cur, conn)
        cur.close()
        conn.close()
    else:
        messagebox.showinfo("Error", "Wrong login or password!")

def clear(loginEntry, passwordEntry):
    loginEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')

def mainMenu():
    window = tkinter.Tk()
    window.title("Library Server")
    window.geometry("195x160")
    welcomeLabel = tkinter.Label(text="Hello! Welcome to the library server")
    welcomeLabel.grid(column=0, row=0)
    loginLabel = tkinter.Label(text="Write login:")
    loginLabel.grid(column=0, row=1)
    loginEntry = tkinter.Entry(window, width=20)
    loginEntry.grid(column=0, row=2)
    passwordLabel = tkinter.Label(text="Write password:")
    passwordLabel.grid(column=0, row=3)
    passwordEntry = tkinter.Entry(window, width=20)
    passwordEntry.grid(column=0, row=4)
    btnGuest = ttk.Button(window, text="Guest access", command=lambda:getGuestAccess(window))
    btnGuest.grid(column=0, row=5)
    btnCheck = ttk.Button(window, text="Enter", command=lambda:getTxt(loginEntry, passwordEntry, window))
    btnCheck.grid(column=0, row=6)
    window.mainloop()