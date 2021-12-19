#imports
from os import times
from tkinter import *
from tkinter import font
from tkinter import filedialog
import math
import threading
from game_logic import check,ai,place,get_board,resetboard
#Root configi
root = Tk()
root.geometry("1870x960")
root.title("Tic Tac Toe GUI")
#This is for tranfering moves to number values
dict_items = {
            "1":"1,1","2":"1,2","3":"1,3",
            "4":"2,1","5":"2,2","6":"2,3",
            "7":"3,1","8":"3,2","9":"3,3"
            }
            
#Output Var
output = StringVar()
output.set("This is where the messages go")
x1_y1 = StringVar()
x1_y1.set("-")
x2_y1 = StringVar()
x2_y1.set("-")
x3_y1 = StringVar()
x3_y1.set("-")
x1_y2 = StringVar()
x1_y2.set("-")
x2_y2 = StringVar()
x2_y2.set("-")
x3_y2 = StringVar()
x3_y2.set("-")
x1_y3 = StringVar()
x1_y3.set("-")
x2_y3 = StringVar()
x2_y3.set("-")
x3_y3 = StringVar()
x3_y3.set("-")

#Varriables used in Font sizes
increseRatio= 1.5
decreaseRatio = 0.9

#Font spesific function
fontsizestrvar = StringVar()
fontsizestrvar.set("11")
def getFont(size):
    fontsizestr = fontsizestrvar.get()
    fontsize =int(math.log(int(fontsizestr)* int(math.sqrt(xsize()*ysize()))))
    fonttype = "Ariel "
    if size == "reg":
        fontTotalreg = fonttype + str(fontsize)
        return fontTotalreg
    if size == "small":
        fontTotalsmall = fonttype + str(int(fontsize*decreaseRatio))
        return fontTotalsmall
    if size == "big":
        fontTotalBig = fonttype + str(int(fontsize*increseRatio))
        return fontTotalBig

#Function that creates widjets, and edits their proporties
def createLables():
    #Title Label 
    title_lbl.config(
                    text = "Welcome to Tic-Tac-Toe", 
                    background ="lightSteelBlue4",
                    font = getFont("big")
                    )
    output_lbl.config(
                    textvariable = output, 
                    background ="lightSteelBlue4",
                    font = getFont("big")
                    )
def createBtn():
    #Position buttons
    btn_x1_y1.config(
                    textvariable=x1_y1,
                    command=place_x1_y1, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x2_y1.config(
                    textvariable=x2_y1,
                    command=place_x2_y1, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x3_y1.config(
                    textvariable=x3_y1,
                    command=place_x3_y1, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x1_y2.config(
                    textvariable=x1_y2,
                    command=place_x1_y2, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x2_y2.config(
                    textvariable=x2_y2,
                    command=place_x2_y2, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x3_y2.config(
                    textvariable=x3_y2,
                    command=place_x3_y2, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x1_y3.config(
                    textvariable=x1_y3,
                    command=place_x1_y3, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x2_y3.config(
                    textvariable=x2_y3,
                    command=place_x2_y3, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_x3_y3.config(
                    textvariable=x3_y3,
                    command=place_x3_y3, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
    btn_reset.config(
                    text="Reset button",
                    command=reset_btn_func, 
                    background="lightSteelBlue4",
                    font= getFont("reg"),
                    wrap= xsize()/8                  
                    )
#Click Functions
#These Functions make it so that when you click their respective button they perform the action that they are linked to above
def ai_move(move):
    placement = dict_items[str(move)]
    if placement == "1,1":
        x1_y1.set("0")
    if placement == "1,2":
        x2_y1.set("0")
    if placement == "1,3":
        x3_y1.set("0")
    if placement == "2,1":
        x1_y2.set("0")
    if placement == "2,2":
        x2_y2.set("0")
    if placement == "2,3":
        x3_y2.set("0")
    if placement == "3,1":
        x1_y3.set("0")
    if placement == "3,2":
        x2_y3.set("0")
    if placement == "3,3":
        x3_y3.set("0")
def place_x1_y1():
    player_move = place(1,1,1)
    if player_move == "You have done a succsess full move":
        x1_y1.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x2_y1():
    player_move = place(1,2,1)
    if player_move == "You have done a succsess full move":
        x2_y1.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x3_y1():
    player_move = place(1,3,1)
    if player_move == "You have done a succsess full move":
        x3_y1.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x1_y2():
    player_move = place(2,1,1)
    if player_move == "You have done a succsess full move":
        x1_y2.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x2_y2():
    player_move = place(2,2,1)
    if player_move == "You have done a succsess full move":
        x2_y2.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x3_y2():
    player_move = place(2,3,1)
    if player_move == "You have done a succsess full move":
        x3_y2.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x1_y3():
    player_move = place(3,1,1)
    if player_move == "You have done a succsess full move":
        x1_y3.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x2_y3():
    player_move = place(3,2,1)
    if player_move == "You have done a succsess full move":
        x2_y3.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def place_x3_y3():
    player_move = place(3,3,1)
    if player_move == "You have done a succsess full move":
        x3_y3.set("X")
        move = ai(get_board())
        print(move)
        for i in get_board():
            print(i)
        if move > 0:
            ai_move(move)
        if check(get_board()) != 0 and check(get_board()) < 3:
            output.set(f"Player {check(get_board())} Won")
        if check(get_board()) == 3:
           output.set(f"Tie") 
    else:
        output.set(f"{player_move}")
def reset_btn_func():
    resetboard()
    print(get_board())
    x1_y1.set("-")
    x2_y1.set("-")
    x3_y1.set("-")
    x1_y2.set("-")
    x2_y2.set("-")
    x3_y2.set("-")
    x1_y3.set("-")
    x2_y3.set("-")
    x3_y3.set("-")


#Funtion used for calculating spacing
def spacing():
    #creates Widgets
    createBtn()
    createLables()

    #spesific colums
    colum1= 0.5/7
    colum2=1.5/7
    colum3=2.5/7
    colum4=3.5/7
    colum5=4.5/7
    colum6=5.5/7
    colum7=6.5/7

    #constants
    widWidth =1/7
    widHeight = 1/8

    #spesific rows
    row1 = 0.5/5
    row2 = 1.5/5
    row3 = 2.5/5
    row4 = 3.5/5
    row5 = 4/5

    #Makes a bar the whole width of the screen
    widWidthFull = 1

    #Lables
    #Title Label
    title_lbl.place(
                    anchor= N, 
                    relx =  colum4, 
                    rely = row1, 
                    relwidth= widWidthFull,
                    relheight= widHeight
                    )
    output_lbl.place(
                    anchor= N, 
                    relx =  colum4, 
                    rely = row5, 
                    relwidth= widWidthFull,
                    relheight= widHeight
                    )
    #Standard Buttons
    #Positioning buttons
    btn_x1_y1.place(
                    anchor= N, 
                    relx = colum3, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x2_y1.place(
                    anchor= N, 
                    relx = colum4, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x3_y1.place(
                    anchor= N, 
                    relx = colum5, 
                    rely = row2, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x1_y2.place(
                    anchor= N, 
                    relx = colum3, 
                    rely = row3, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x2_y2.place(
                    anchor= N, 
                    relx = colum4, 
                    rely = row3, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x3_y2.place(
                    anchor= N, 
                    relx = colum5, 
                    rely = row3, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x1_y3.place(
                    anchor= N, 
                    relx = colum3, 
                    rely = row4, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x2_y3.place(
                    anchor= N, 
                    relx = colum4, 
                    rely = row4, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_x3_y3.place(
                    anchor= N, 
                    relx = colum5, 
                    rely = row4, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    btn_reset.place(
                    anchor= N, 
                    relx = colum2, 
                    rely = row3, 
                    relwidth= widWidth, 
                    relheight= widHeight,
                    )
    #runs the command every 0.1 second
    threading.Timer(0.1, spacing).start()
def ysize():
    alllist=root.winfo_geometry()
    splitlist = alllist.split("+")
    xylist= splitlist[0].split("x")
    yvar = xylist[1]
    xvar = xylist[0]
    return int(yvar)
def xsize():
    alllist=root.winfo_geometry()
    splitlist = alllist.split("+")
    xylist= splitlist[0].split("x")
    yvar = xylist[1]
    xvar = xylist[0]
    return int(xvar)

#function that runs once the start button is clicked
def start():
    btn_Start.destroy()
    spacing()
    resetboard()

#Labels
title_lbl = Label(root)
output_lbl = Label(root)
#Buttons
btn_x1_y1 = Button(root)
btn_x2_y1 = Button(root)
btn_x3_y1 = Button(root)
btn_x1_y2 = Button(root)
btn_x2_y2 = Button(root)
btn_x3_y2 = Button(root)
btn_x1_y3 = Button(root)
btn_x2_y3 = Button(root)
btn_x3_y3 = Button(root)
btn_reset = Button(root)
#Creates the start button, This is required in order to kick off the program to reduce lag
btn_Start = Button(
                    root,
                     text = "Start Button", 
                     command=start,
                     background="LightSteelBlue2", 
                     font="Arial 50", 
                     width=10,
                     height=5
                   )
    


#Positioning start button
btn_Start.place(anchor=N, relx = 0.5, rely= 0.25)

#main root loop
root.mainloop()