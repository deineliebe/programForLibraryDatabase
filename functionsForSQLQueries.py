import tkinter
from tkinter import messagebox
from datetime import date
from datetime import datetime

#Functions for buttons
def queryToAnObject(queries, mes, window, cur, conn):
    try:
        for query in queries:
            cur.execute(query)
        conn.commit()
        messagebox.showinfo("Well done!", mes)
        window.destroy()
    except:
        messagebox.showinfo("Error", "Unknown error. Check your data")
        cur.close()
        cur = conn.cursor()

def fillList(cur, lis, query, number):
    cur.execute(query)
    info = cur.fetchall()
    arr = list()
    for row in info:
        arr.append(row[number])
    lis['values'] = arr

def fillEntries(cur, query, indexes, entries):
    cur.execute(query)
    info = cur.fetchall()
    for row in info:
        for i in range(len(indexes)):
            entries[i].delete(0, 'end')
            entries[i].insert(0, row[indexes[i]])

def showElem(cur, query, indexes, labelsName):
    cur.execute(query)
    info = cur.fetchall()
    for row in info:
        for i in range(len(indexes)):
            labelsName[i]['text'] = row[indexes[i]]

def reference(cur, txt, query):
    txt.delete('1.0', tkinter.END)
    cur.execute(query)
    info = cur.fetchall()
    for row in info:
        txt.insert(tkinter.INSERT, str(row[0]) + " in " + str(row[1]) + " hall: " + str(row[2]) + "\n")

def fillTxt(cur, txt, query):
    cur.execute(query)
    info = cur.fetchall()
    for row in info:
        txt.insert(tkinter.INSERT, str(row[0]) + "\n")

#Errors
def checkBook(cur, query, labelName):
    cur.execute(query)
    info = cur.fetchall()
    if (len(info)):
        labelName['text'] = "Book is in the library!"
    else:
        labelName['text'] = "There isn't book with this name"

def checkLen(word, maxLength, name):
    if (len(str(word)) > maxLength):
        messagebox.showinfo("Error", "Max length of parameter " + name + " is " + str(maxLength) + " symbols")
        return 0
    return 1

def checkIfOnlyLetters(word, name):
    if (word.isalpha()):
        return 1
    messagebox.showinfo("Error", "Parameter " + name + " must contain only letters")
    return 0

def checkIfIsNull(word, name):
    if (len(word)):
        return 1
    messagebox.showinfo("Error", "Please, fill parameter " + name + "! It mustn't be a null")
    return 0

def checkIfDigit(word, name):
    if (word.isdigit()):
        return 1
    messagebox.showinfo("Error", "Parameter " + name + " must be a number")
    return 0

def checkIfThisYearOrEarlier(word):
    if (int(word) > date.today().year):
        messagebox.showinfo("Error", "Year of the release of the book must be this year or earlier")
        return 0
    return 1

def checkIfPositive(word, name):
    if (int(word) < 0):
        messagebox.showinfo("Error", "Parameter " + name + " must be a positive number")
        return 0
    return 1

#Column errors
def checkSurname(word):
    if (checkIfIsNull(word, "surname") and checkIfOnlyLetters(word, "surname") and checkLen(word, 45, "surname")):
        return 1
    return 0

def checkPhoneNumber(word):
    if (checkLen(word, 16, "phone number") == 0):
        return 0
    if (checkIfIsNull(word, "phone number") == 0):
        return 0
    if (word[0] != '+'):
        messagebox.showinfo("Error", "First symbol of parameter phone number must be a '+'")
        return 0
    if (str(word)[1:].isdigit() == 0):
        messagebox.showinfo("Error", "Parameter phone number must contain only sign '+' and digits")
        return 0
    return 1

def checkLibraryCard(word):
    if (checkIfIsNull(word, "library card") and checkLen(word, 30, "library card")):
        return 1
    return 0

def checkHall(word):
    if (checkIfIsNull(word, "hall") and checkIfOnlyLetters(word, "hall") and checkLen(word, 20, "hall")):
        return 1
    return 0

def checkCapacity(word):
    if (checkIfDigit(str(word), "capacity") and checkIfPositive(int(word), "capacity")):
        return 1
    return 0

def checkBookName(word):
    if (checkIfIsNull(word, "book") and checkLen(word, 50, "book")):
        return 1
    return 0

def checkAuthor(word):
    if (checkIfIsNull(word, "author") and checkIfOnlyLetters(word, "author") and checkLen(word, 45, "author")):
        return 1
    return 0

def checkYear(word):
    if (checkIfIsNull(word, "year") and checkIfDigit(word, "year") and checkIfPositive(word, "year") and checkIfThisYearOrEarlier(word)):
        return 1
    return 0

def checkCypher(word):
    if (checkIfIsNull(word, "cypher") and checkLen(word, 40, "cypher")):
        return 1
    return 0

def checkCnt(word):
    if (checkIfIsNull(word, "cnt") and checkIfDigit(word, "cnt") and checkIfPositive(word, "cnt")):
        return 1
    return 0

def checkIfNotExist(tableName, columnName, criterion, cur):
    cur.execute("SELECT * FROM " + tableName + " WHERE " + columnName + " = '" + criterion + "'")
    info = cur.fetchall()
    if (info):
        return 1
    messagebox.showinfo("Error", "There aren't elemints in " + columnName + " equal to " + criterion)
    return 0

def checkIfExist(tableName, columnName, criterion, cur, prev=""):
    cur.execute("SELECT * FROM " + tableName + " WHERE " + columnName + " = '" + criterion + "'")
    info = cur.fetchall()
    if (len(info) > 0 and criterion != prev):
        messagebox.showinfo("Error", "Mean of column " + columnName + ", " + criterion + ", must be unique")
        return 0
    return 1

#Additional errors
def addReader(surname, phone, libraryCard, hall, window, cur, conn):
    if (checkSurname(surname) and checkPhoneNumber(phone) and checkLibraryCard(libraryCard) and checkIfExist("readers", "library_card", libraryCard, cur) and checkIfNotExist("halls", "name", hall, cur) and checkHall(hall)):
        queryToAnObject(["INSERT INTO readers(surname, phone, library_card) VALUES('" + surname + "', '" + phone + "', '" + libraryCard + "')", "INSERT INTO readers_halls(library_card, hall) VALUES('" + libraryCard + "', '" + hall + "')"], "New reader added", window, cur, conn)

def addHall(name, capacity, window, cur, conn):
    if (checkHall(name) and checkIfExist("halls", "name", name, cur) and checkCapacity(capacity)):
        queryToAnObject(["INSERT INTO halls(name, capacity) VALUES('" + name + "', " + capacity + ")"], "New hall added", window, cur, conn)

def addBook(name, author, year, cypher, hall, cnt, window, cur, conn):
    if (checkBookName(name) and checkAuthor(author) and checkYear(year) and checkCypher(cypher) and checkIfExist("books", "cypher", cypher, cur) and checkIfNotExist("halls", "name", hall, cur) and checkHall(hall) and checkCnt(cnt)):
        queryToAnObject(["INSERT INTO books(name, author, year, cypher) VALUES('" + name + "', '" + author + "', " + year + ", '" + cypher + "')", "INSERT INTO books_halls(cypher, hall, cnt) VALUES('" + cypher + "', '" + hall + "', " + cnt + ")"], "New book added", window, cur, conn)

def addRecord(library_card, cypher, window, cur, conn):
    if (checkLibraryCard(library_card) and checkIfNotExist("readers", "library_card", library_card, cur) and checkCypher(cypher) and checkIfNotExist("books", "cypher", cypher, cur)):
        queryToAnObject(["INSERT INTO books_readers(library_card, cypher, date) VALUES('" + library_card + "', '" + cypher + "', '" + datetime.today().strftime('%Y-%m-%d') + "')"], "New record added", window, cur, conn)

#Update errors
def updateReader(surname, phone, libraryCard, hall, criterion, window, cur, conn):
    if (checkSurname(surname) and checkPhoneNumber(phone) and checkLibraryCard(libraryCard) and checkIfExist("readers", "library_card", libraryCard, cur, criterion) and checkIfNotExist("halls", "name", hall, cur) and checkHall(hall)):
        queryToAnObject(["UPDATE readers SET surname = '" + surname + "', phone = '" + phone + "', library_card = '" + libraryCard + "' WHERE library_card = '" + criterion + "'", "UPDATE books_readers SET library_card = '" + libraryCard + "' WHERE library_card = '" + criterion + "'", "UPDATE readers_halls SET hall = '" + hall + "', library_card = '" + libraryCard + "' WHERE library_card = '" + criterion + "'"], "Reader was updated", window, cur, conn)

def updateHall(name, capacity, criterion, window, cur, conn):
    if (checkHall(name) and checkIfExist("halls", "name", name, cur, criterion) and checkCapacity(capacity)):
        queryToAnObject(["UPDATE halls SET name = '" + name + "', capacity = " + str(capacity) + " WHERE name = '" + criterion + "'", "UPDATE books_halls SET hall = '" + name + "' WHERE hall = '" + criterion + "'", "UPDATE readers_halls SET hall = '" + name + "' WHERE hall = '" + criterion + "'"], "Hall was updated", window, cur, conn)

def updateBook(name, author, year, cypher, criterion, window, cur, conn):
    if (checkBookName(name) and checkAuthor(author) and checkYear(year) and checkCypher(cypher) and checkIfExist("books", "cypher", cypher, cur, criterion)):
        queryToAnObject(["UPDATE books SET name = '" + name + "', author = '" + author + "', year = " + year + ", cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'", "UPDATE books_halls SET cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'", "UPDATE books_readers SET cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'"], "Book was updated", window, cur, conn)

def updateBookCypher(cypher, criterion, window, cur, conn):
    if (checkCypher(cypher) and checkIfExist("books", "cypher", cypher, cur, criterion)):
        queryToAnObject(["UPDATE books SET cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'", "UPDATE books_halls SET cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'", "UPDATE books_readers SET cypher = '" + cypher + "' WHERE cypher = '" + criterion + "'"], "Book was updated", window, cur, conn)