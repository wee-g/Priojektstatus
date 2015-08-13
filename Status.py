__author__ = 'stefanwitschi'

import tkinter, tkinter.messagebox, os, sqlite3
from tkinter import *
from tkinter import ttk


# HAUPTFENSTER ERSTELLEN
main = tkinter.Tk()
main.geometry("%dx%d+%d+%d" % (600, 700, 600, 100))
main.title("Projekt Status")

# FRAMES ERSTELLEN

labelframe1 = LabelFrame(main, text="Projekt", width=300, height=20,
                         pady=10, padx=10, font="Verdana 10 ")
labelframe1.pack(fill=X)

labelframe2 = LabelFrame(main, text="Status", width=300, height = 400,
                         pady=10, padx=10, font = "Verdana 10 ")
labelframe2.pack(fill=X)

labelframe3 = LabelFrame(main, text="Bemerkungen", width=300, height = 400,
                         pady=10, padx=10, font = "Verdana 10 ")
labelframe3.pack(fill=X)

# INFOTEXTE

def msginfo1():
    tkinter.messagebox.showinfo \
       ("Warnung","Bitte bei Da nur Zahl eingeben")

def msginfo2(projekt, fa, ag):
    tkinter.messagebox.showinfo \
       ("Warnung","Projekt " + projekt + " " + fa + " " + ag + " nicht vorhanden")

def msginfo3(projekt, fa, ag):
    tkinter.messagebox.showinfo \
       ("Warnung","Projekt " + projekt + " " + fa + " " + ag  + " eingetragen")

def msginfo4(projekt, fa, ag):
    tkinter.messagebox.showinfo \
       ("Warnung","Projekt " + projekt + " " + fa + " " + ag + " gelöscht")

def msginfo5(projekt, fa, ag):
    tkinter.messagebox.showinfo \
       ("Warnung","Projekt " + projekt + " " + fa + " " + ag + " schon vorhanden")

def msginfo6(projekt, fa, ag):
    tkinter.messagebox.showinfo \
       ("Warnung","Projekt " + projekt + " " + fa + " " + ag + " geändert")



# MENUELEISTE

def ende():
    main.destroy()

# Infotext fuer About

def msginfo():

    textabout = """

Projekt Status

Datenbank: T:\Python_Programme\Status.db

V1.0 (Beta)

30.4.2015 S.Witschi"""

    tkinter.messagebox.showinfo \
       ("About",textabout)

def infotest():
    child1= tkinter.Tk()
    sizex= 500
    sizey= 600
    posx= 300
    posy= 100
    child1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    child1.wm_title("Projekt Status")

#    tkinter.messagebox.showinfo \
#       ("Hilfe","in Bearbeitung")

def info1():

    texthelp = """


Info zu Projekt Status Datenbank



"""

    tkinter.messagebox.showinfo \
       ("Hilfe",texthelp)

def info2():

    texthelp = """


Text hier eintragen

"""

    tkinter.messagebox.showinfo \
        ("Hilfe",texthelp)



# VERSCHLUESSELUNG

key =14

def verschluesselterText(klartext, schluessel):
    geheimtext = ''
    for zeichen in klartext:
        zahl = ord(zeichen)
        neuezahl = zahl + schluessel
        #if neuezahl > ord('Z'):
            #neuezahl = neuezahl - 26
        neuesZeichen = chr(neuezahl)
        geheimtext = geheimtext + neuesZeichen
    return geheimtext


def klartext(geheimtext, schluessel):
    klartext = ''
    for zeichen in geheimtext:
        zahl = ord(zeichen)
        neuezahl = zahl - schluessel
        neuesZeichen = chr(neuezahl)
        klartext = klartext + neuesZeichen
    return klartext


# DATENBANK

pfad = "/Volumes/home/Dokumente/Python/Fertige_Programme/Datenbanken/projektstatusex.db"


# Eröffnen einer Datenbank

# Existenz feststellen
if os.path.exists(pfad):
    print("")

else:

    # Verbindung zur Datenbank erzeugen
    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    # Tabelle erzeugen
    sql = "CREATE TABLE projectstatus(" \
        "projekt TEXT  , " \
        "fa TEXT, " \
        "ag TEXT, " \
        "status TEXT, " \
        "bemerkungen TEXT)"
    cursor.execute(sql)

     #    Datensatz erzeugen
    sql = "INSERT INTO projectstatus (projekt,fa,ag,status,bemerkungen) VALUES('?','?','?','?','?')"
    cursor.execute(sql)
    connection.commit()

    # Verbindung beenden
    connection.close()


# Eröffnen Datenbank letzter Eintrag

    # Verbindung zur Datenbank erzeugen
    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    # Tabelle erzeugen
    sql1 = "CREATE TABLE lastentry(" \
        "ID INTEGER  , " \
        "projekt TEXT  , " \
        "fa TEXT, " \
        "ag TEXT, " \
        "status TEXT, " \
        "bemerkungen TEXT)"
    cursor.execute(sql1)
    print("xxxxxxxxxxxx")
     #    Datensatz erzeugen
    sql1 = "INSERT INTO lastentry (ID,projekt,fa,ag,status,bemerkungen) VALUES(1,'?','?','?','?','?')"
    cursor.execute(sql1)
    connection.commit()

    # Verbindung beenden
    connection.close()


# EINGABE

# Projekt

inputprojekt = tkinter.Entry(labelframe1, width=20)
inputprojekt.focus_set()
inputprojekt.grid(row=0, column=1, sticky=W, padx=5)
#inputtool.bind("<Return>", anzeigen)
textprojekt = tkinter.Label(labelframe1,  text="Projekt")
textprojekt.grid(row=0, column=0, sticky=W)

# FA-Nummer

inputfa = tkinter.Entry(labelframe1, width=20)
inputfa.focus_set()
inputfa.grid(row=1, column=1, sticky=W,padx=5)
#inputtool.bind("<Return>", anzeigen)
textfa = tkinter.Label(labelframe1, text="FA-Nummer")
textfa.grid(row=1, column=0, sticky = W)

# AG

inputag = tkinter.Entry(labelframe1, width=20)
inputag.focus_set()
inputag.grid(row=2, column=1, sticky=W,  padx=5)
#inputtool.bind("<Return>", anzeigen)
textag = tkinter.Label(labelframe1, text="AG")
textag.grid(row=2, column=0, sticky=W)

# AG

inputstatus = tkinter.Entry(labelframe2, width=20)
inputstatus.focus_set()
inputstatus.grid(row=0, column=0, sticky=W,  padx=5)
#inputtool.bind("<Return>", anzeigen)

# Status

inputbemerkung = Text(labelframe3, height=20, width=50)
inputbemerkung.grid(row=0, column=0, sticky=W, padx=1, columnspan=2)

def clear():
    inputprojekt.delete(0, END)
    inputfa.delete(0, END)
    inputag.delete(0, END)
    inputstatus.delete(0, END)
    inputbemerkung.delete("1.0",'end-1c')

def lastentry():
    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM lastentry WHERE ID  = 1')

    rows = cursor.fetchall()
    if len(rows) == 0:
        msginfo2(projekt, fa, ag)
        return

#    print(rows)
    for entry in rows:
        # print(entry)


        entry1 = klartext(entry[1], key)
        entry2 = klartext(entry[2], key)
        entry3 = klartext(entry[3], key)
        entry4 = klartext(entry[4], key)
        entry5 = klartext(entry[5], key)


        inputprojekt.delete(0, END)
        inputprojekt.insert(0, entry1)
        inputfa.delete(0, END)
        inputfa.insert(0, entry2)
        inputag.delete(0, END)
        inputag.insert(0, entry3)
        inputstatus.delete(0, END)
        inputstatus.insert(0, entry4)
        inputbemerkung.delete("1.0",'end-1c')
        inputbemerkung.insert(END, entry5)
    # Verbindung beenden
    connection.close()



def anzeigen():
    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    projekt = inputprojekt.get()
    fa = inputfa.get()
    ag = inputag.get()

    projektcrypt = verschluesselterText(projekt, key)
    facrypt = verschluesselterText(fa, key)
    agcrypt = verschluesselterText(ag, key)


    t=(projektcrypt, facrypt, agcrypt)
    cursor.execute('SELECT * FROM projectstatus WHERE projekt LIKE ? AND fa = ? AND ag = ?', t)

    rows = cursor.fetchall()
    if len(rows) == 0:
        msginfo2(projekt, fa, ag)
        return

#    print(rows)
    for entry in rows:
        # print(entry)


        entry4 = klartext(entry[4], key)
        entry3 = klartext(entry[3], key)

        inputbemerkung.delete("1.0",'end-1c')
        inputbemerkung.insert(END, entry4)
        inputstatus.delete(0, END)
        inputstatus.insert(0, entry3)


        #inputbemerkung.delete("1.0",'end-1c')
        #inputbemerkung.insert(END, entry[4])
        #inputstatus.delete(0, END)
        #inputstatus.insert(0, entry[3])


    # Verbindung beenden
    connection.close()





def loeschen():
    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    projekt = inputprojekt.get()
    fa = inputfa.get()
    ag = inputag.get()

    loeschenyesno = tkinter.messagebox.askyesno \
       (message="Projekt " + projekt + " " + fa + " " + ag + " löschen?"
        , title="Löschen", icon='question')

    if loeschenyesno == True:


        projektcrypt = verschluesselterText(projekt, key)
        facrypt = verschluesselterText(fa, key)
        agcrypt = verschluesselterText(ag, key)



        t=(projektcrypt, facrypt, agcrypt)
        cursor.execute('DELETE FROM projectstatus WHERE projekt LIKE ? AND fa = ? AND ag = ?', t)

        connection.commit()
        clear()
        msginfo4(projekt, fa, ag)

    else:
        tkinter.messagebox.showinfo \
        ("Löschen","Projekt " + projekt + " " + fa + " " + ag + " nicht gelöscht")

    # Verbindung beenden
    connection.close()


def eintragen():

    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    projekt = inputprojekt.get()
    fa = inputfa.get()
    ag = inputag.get()
    status = inputstatus.get()
    bemerkung = inputbemerkung.get("1.0",'end-1c')


    projektcrypt = verschluesselterText(projekt, key)
    facrypt = verschluesselterText(fa, key)
    agcrypt = verschluesselterText(ag, key)
    statuscrypt = verschluesselterText(status, key)
    bemerkungcrypt = verschluesselterText(bemerkung, key)


    t=(projektcrypt, facrypt, agcrypt)
    cursor.execute('SELECT * FROM projectstatus WHERE projekt LIKE ? AND fa = ? AND ag = ?', t)

    rows = cursor.fetchall()

    if len(rows) > 0:
        msginfo5(projekt, fa, ag)
        return


    werte = [projektcrypt,facrypt,agcrypt,statuscrypt,bemerkungcrypt]

    # Datensatz erzeugen

    sql = "INSERT INTO projectstatus VALUES(?,?,?,?,?)"

    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    cursor.execute(sql, werte)

    cursor.execute("UPDATE lastentry SET projekt = ? WHERE ID  = ?",(projektcrypt,1))
    cursor.execute("UPDATE lastentry SET fa = ? WHERE ID  = ?",(facrypt,1))
    cursor.execute("UPDATE lastentry SET ag = ? WHERE ID  = ?",(agcrypt,1))
    cursor.execute("UPDATE lastentry SET status = ? WHERE ID  = ?",(statuscrypt,1))
    cursor.execute("UPDATE lastentry SET bemerkungen = ? WHERE ID = ?",(bemerkungcrypt,1))

    # Dummy Datensatz löschen

    cursor.execute("DELETE FROM projectstatus WHERE projekt = ?",("?"))

    connection.commit()
    msginfo3(projekt, fa, ag)

    # Verbindung beenden
    connection.close()

# DATENSAETZE AENDERN

def aendern():

    connection = sqlite3.connect(pfad)

    # Datensatzcursor erzeugen
    cursor = connection.cursor()

    projekt = inputprojekt.get()
    fa = inputfa.get()
    ag = inputag.get()
    status = inputstatus.get()
    bemerkung = inputbemerkung.get("1.0",'end-1c')

    aendern = tkinter.messagebox.askyesno \
        (message="Status und/oder Bemerkung äendern ?"
        ,title="Ändern",icon='question')

    if aendern == True:


        projektcrypt = verschluesselterText(projekt, key)
        facrypt = verschluesselterText(fa, key)
        agcrypt = verschluesselterText(ag, key)
        statuscrypt = verschluesselterText(status, key)
        bemerkungcrypt = verschluesselterText(bemerkung, key)



        t=(projektcrypt, facrypt, agcrypt)
        tx=(statuscrypt,projektcrypt, facrypt, agcrypt)
        txx=(bemerkungcrypt,projektcrypt, facrypt, agcrypt)
        cursor.execute('SELECT * FROM projectstatus WHERE projekt LIKE ? AND fa = ? AND ag = ?', t)

        rows = cursor.fetchall()

        if len(rows) < 1:
            msginfo2(projekt, fa, ag)
            return

        cursor.execute("UPDATE projectstatus SET status = ? WHERE projekt LIKE ? AND fa = ? AND ag = ?", tx)
        cursor.execute("UPDATE projectstatus SET bemerkungen = ? WHERE projekt LIKE ? AND fa = ? AND ag = ?", txx)
        cursor.execute("UPDATE lastentry SET projekt = ? WHERE ID  = ?",(projektcrypt,1))
        cursor.execute("UPDATE lastentry SET fa = ? WHERE ID  = ?", (facrypt,1))
        cursor.execute("UPDATE lastentry SET ag = ? WHERE ID  = ?" ,(agcrypt,1))
        cursor.execute("UPDATE lastentry SET status = ? WHERE ID  = ?", (statuscrypt,1))
        cursor.execute("UPDATE lastentry SET bemerkungen = ? WHERE ID = ?", (bemerkungcrypt,1))

        connection.commit()

        msginfo6(projekt, fa, ag)

    else:
        tkinter.messagebox.showinfo \
        ("Ändern","Status nicht geändert")

    # Verbindung beenden
    connection.close()

# Alle Anzeigen

def suche():

    connection = sqlite3.connect(pfad)


    # Datensatzcursor erzeugen
    cursor = connection.cursor()


    cursor.execute("SELECT projekt, fa, ag, status from projectstatus ORDER BY projekt")

    rows = cursor.fetchall()

    #print(rows)


    #rows = (klartext(cursor.fetchall(), key))
    #print("rows",rows)

    numrows = len(rows)

    #print(str(numrows) + " Datensätze gefunden")

    return (numrows, rows)

def alleanz():

    def data():


        columntree = ttk.Treeview(framechi, show=["headings"],
                                       selectmode="extended")
        columntree.pack()
        columntree["columns"]=("projekt","fa","ag","status")
        columntree.heading("projekt", text="Projekt")
        columntree.column("projekt", width=120, anchor="w")
        columntree.heading("fa", text="FA")
        columntree.column("fa", width=80, anchor="w")
        columntree.heading("ag", text="AG")
        columntree.column("ag", width=80)
        columntree.heading("status", text="Status")
        columntree.column("status", width=80)

        """
        def copyclip(event):
            selected = columntree.selection()
            main.clipboard_append(str(selected))
        columntree.bind('<Control-c>', copyclip)
        """


        def OnDoubleClick(event):


            # .focus() gives me the row ID I've double-clicked on
            cRowId = columntree.focus()
            # .item() gives me a dictionary of that row's info
            dicTemp = columntree.item(cRowId)["values"]
            print( dicTemp )

            connection = sqlite3.connect(pfad)

            # Datensatzcursor erzeugen
            cursor = connection.cursor()

            projekt = str(dicTemp[0])
            fa = str(dicTemp[1])
            ag = str(dicTemp[2])
            print(projekt)

            projektcrypt = verschluesselterText(projekt, key)
            facrypt = verschluesselterText(fa, key)
            agcrypt = verschluesselterText(ag, key)


            t=(projektcrypt, facrypt, agcrypt)
            cursor.execute('SELECT * FROM projectstatus WHERE projekt LIKE ? AND fa = ? AND ag = ?', t)

            rows = cursor.fetchall()
            if len(rows) == 0:
                msginfo2(projekt, fa, ag)
                return

        #    print(rows)
            for entry in rows:
                # print(entry)


                entry0 = klartext(entry[0], key)
                entry1 = klartext(entry[1], key)
                entry2 = klartext(entry[2], key)
                entry3 = klartext(entry[3], key)
                entry4 = klartext(entry[4], key)

                inputprojekt.delete(0, END)
                inputprojekt.insert(0, entry0)

                inputfa.delete(0, END)
                inputfa.insert(0, entry1)

                inputag.delete(0, END)
                inputag.insert(0, entry2)

                inputbemerkung.delete("1.0",'end-1c')
                inputbemerkung.insert(END, entry4)
                inputstatus.delete(0, END)
                inputstatus.insert(0, entry3)

        columntree.bind("<Double-1>", OnDoubleClick)
        (numrows, rows) = suche()



        i = 0
        for entry in rows:
            entry = list(entry)
            newrows=[]

            for x in entry:
                x = klartext(x, key)
                newrows.append(x)


            if i % 2:
                columntree.insert("", "end", text=newrows[0], values=(newrows),
                                       tags=("oddrow"))
            else:
                columntree.insert("", "end", text=newrows[0], values=(newrows),
                                       tags=("evenrow"))
            i+=1
        columntree.tag_configure("oddrow", background="#d0e2f9")
        columntree.tag_configure("evenrow", background="#eff2f5")



    def ende1():
        child1.destroy()

    # Scrollbar erzeugen


    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"),width=80,height=300)


    child1 = tkinter.Tk()
    sizex = 400
    sizey = 300
    posx  = 800
    posy  = 150
    child1.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
    child1.wm_title("Datenbank")

    chi1=tkinter.Frame(child1,relief=GROOVE,width=500,height=100,bd=1)
    chi1.pack()

    canvas=Canvas(chi1, width=400)
    framechi=Frame(canvas)
    vscrollbar=Scrollbar(chi1,orient="vertical",command=canvas.yview)
    hscrollbar=Scrollbar(chi1,orient="horizontal",command=canvas.xview)
    canvas.configure(yscrollcommand=vscrollbar.set)
    canvas.configure(xscrollcommand=hscrollbar.set)

    vscrollbar.pack(side="right",fill="y")
    hscrollbar.pack(side="bottom",fill="x")
    canvas.pack(side="left")
    canvas.create_window((0,0),window=framechi,anchor='nw')
    #framechi.bind("<Configure>",myfunction)
    data()


    child1.mainloop()


# Buttons
banzeigen = tkinter.Button(labelframe1, text="Anzeigen", command=anzeigen, width=8)
banzeigen.grid(row=3, column=0, sticky= W,padx=8, pady=10)

bloeschen = tkinter.Button(labelframe1, text="Loeschen", command=loeschen, width=8)
bloeschen.grid(row=3, column=1, sticky= W,padx=8, pady=10)

bclear = tkinter.Button(labelframe1, text="Clear", command=clear, width=8)
bclear.grid(row=3, column=2, sticky= W,padx=8, pady=10)

balan = tkinter.Button(labelframe1, text="Alle anzeigen", command=alleanz, width=10)
balan.grid(row=3, column=3, sticky= W,padx=8, pady=10)

beintragen = tkinter.Button(labelframe3, text="Eintragen", command=eintragen, width=8)
beintragen.grid(row=1, column=0, sticky= S,padx=5, pady=10)

baendern = tkinter.Button(labelframe3, text="Ändern", command=aendern, width=8)
baendern.grid(row=1, column=1, sticky=S, padx=5, pady=10)

# Info-Label
lbinfo = tkinter.Label(main, text="\N{COPYRIGHT SIGN} S.Witschi 2015" , font=("Helvetica", 8))
lbinfo.place(x = 0, y = 660, width=110, height=30)


# MENUELISTE

# erzeugt gesamte Menuleiste
mBar = tkinter.Menu(main)

# Datei
mFile = tkinter.Menu(mBar)
mFile["tearoff"] = 0     # Menu nicht abtrennbar

# erzeugt Elemente im Menu
mFile.add_command(label="Exit", command=ende)
mFile.add_command(label="Letzter Eintrag", command=lastentry)

# Hilfe
mHelp = tkinter.Menu(mBar)
mHelp["tearoff"] = 0     # Menu nicht abtrennbar

#submHelp = tkinter.Menu(mHelp)
#submHelp["tearoff"] = 0     # Menu nicht abtrennbar

# erzeugt Elemente im Menu
mHelp.add_command(label="About", command=msginfo)
mHelp.add_command(label="Info", command=info1)
#mHelp.add_command(label="Eingabe Verdrehung", command=info2)
#submHelp.add_command(label="FAQ", command=info)

# Menu zur Menuleiste hinzu
mBar.add_cascade(label="Datei", menu=mFile)
mBar.add_cascade(label="Hilfe", menu=mHelp)
#mHelp.add_cascade(label="Hilfe", menu=submHelp, underline=0)
# gesamte Menuleiste zu Fenster hinzu
main["menu"] = mBar



main.mainloop()
