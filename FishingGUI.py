from tkinter import *
import tkinter as tk
import csv
from DiceRoll import Die
global fishGui
global lblFishCaughtHdr
global fishResult
global finalMessage
global fishKept
global lblNumberOfFishKept

#Fish GUI Container
def fishGuiContainer():
    fishGui = tk.Tk()
    fishGui.title("Fishing Application")
    fishGui.geometry("500x500")
    global frameCast
    global frameCastResult
    global frameCastAgain
    global frameCastFinal
    global lblFishCaught
    global lblPointsTally
    global lblNumberOfFishKept
    global lblListOfFishKept
#Frames   
    frameCast = LabelFrame(fishGui, text="Time to throw your line in")
    frameCastResult = LabelFrame(fishGui, text = "Your cast has resulted in catching:")
    frameCastAgain = LabelFrame(fishGui)
    frameCastFinal = LabelFrame(fishGui)
#Container Content  
# Start running score as zero
    global runningScore
    global lblFinalMessage
    global fishKept
    global lblNumberOfFishKept
    fishKept = []
    global lblPointsAccrued
    runningScore = 0

    lblTitle = tk.Label(fishGui, width="500", text = "Catchin Fish", bg = "orange", fg="white").pack(pady=10)
    lblInstructions = tk.Label(fishGui, text="Welcome to Catchin Fish. \n To play this game cast your line, catch a fish and then  \ndecide wether you want to keep it or throw it back").pack(pady=10)
    frameCast.pack()
    cmdCast = tk.Button(frameCast, text="cast", width=10, height=1, bg="green", fg="white", command=rollDICE)
    cmdCast.pack(padx=20,pady=20)
    frameCastResult.pack_forget()
    lblFishCaught = tk.Label (frameCastResult, text = "")
    lblFishCaught.pack()
    lblKeepThrow = tk.Label(frameCastResult, text = "Would you like to keep or release this catch?")
    lblKeepThrow.pack()  
    cmdKeep = tk.Button(frameCastResult, text="KEEP", width=10, height=1, bg="blue", fg="white", command=keepFish)
    cmdKeep.pack()
    cmdRelease = tk.Button(frameCastResult, text="RELEASE", width=10, height=1, bg="blue", fg="white",command=throwFish)
    cmdRelease.pack()
    frameCastAgain.pack_forget()
    lblCastAgain = tk.Label(frameCastAgain, text = "Would you like to cast again?")
    lblCastAgain.pack()
    cmdYes = tk.Button(frameCastAgain, text="YES", width=10, height=1, bg="indigo", fg="white", command=lambda:frameCastAgain.pack_forget() & frameCast.pack())
    cmdYes.pack()
    cmdNo = tk.Button(frameCastAgain, text="NO", width=10, height=1, bg="indigo", fg="white", command=CmdNo)
    cmdNo.pack()
    lblPointsTally = tk.Label(fishGui, text = "Your Points Tally")
    lblPointsTally.pack()
    lblPointsAccrued = tk.Label(fishGui, text = "")
    lblPointsAccrued.pack()
    lblExitThankyou = tk.Label(frameCastFinal, text = "Thankyou for fishing")
    lblExitThankyou.pack()
    lblFinalMessage = tk.Label(frameCastFinal, text = "")
    lblFinalMessage.pack()
    lblNumberOfFishKept = tk.Label(frameCastFinal, text = "")
    lblNumberOfFishKept.pack()
    lblListOfFishKept = tk.Label(frameCastFinal, text = "")
    lblListOfFishKept.pack()
    #cmdExit = tk.Button(frameCastFinal, text="EXIT", width=10, height=1, bg="indigo", fg="white", command=lambda:quit())
    #cmdExit.pack()
    fishGui.mainloop()

#Utilise DiceRoll Class and Fishing CSV to produce random result (rollDICE & GetFish)
def CmdNo():
    frameCastAgain.pack_forget()
    frameCastFinal.pack()
    lblPointsTally.pack_forget()
    lblPointsAccrued.pack_forget()
    writeFinalScoreToCSV()
    print(f"The fish you kept were: {fishKept}")
    fishCount = len(fishKept)
    print(f"You kept: {fishCount} fish")
    numbOfFishMessage = (f"You kept: {fishCount} fish")
    lblNumberOfFishKept["text"] = numbOfFishMessage
    #fishList = (f"{fishKept}")
    Label(frameCastFinal, width=70, bg="orange", text="The Fish You Kept Were: ").pack()
    for fish in fishKept:
        Label(frameCastFinal, width=70, height=2, bg="white", text=f"{fish}").pack()
    cmdExit = tk.Button(frameCastFinal, text="EXIT", width=10, height=1, bg="indigo", fg="white", command=lambda:quit())
    cmdExit.pack(padx=5,pady=5)

def rollDICE():
    diceResult = 0
    create_die = Die(6)
    diceResult = create_die.roll_die()
    GetFish(diceResult)
    lblFishCaught["text"] = fishDisplay
    frameCast.pack_forget()
    frameCastResult.pack()

def keepFish():
    global scoreKeep
    global runningScore
    global finalMessage
    global lblFinalMessage
    global lblPointsAccrued
    #print("Your Keep score is: ")
    #print(scoreKeep)
    runningScore = runningScore + scoreKeep
    finalMessage = (f"{uname} your final score is: {runningScore}")
    lblFinalMessage["text"] = finalMessage
    lblPointsAccrued["text"] = runningScore
    fishKept.append(fishDisplay)
    print(fishKept)
    frameCastResult.pack_forget()
    frameCastAgain.pack()

def throwFish():
    global scoreThrow
    global runningScore
    global finalMessage
    global lblFinalMessage
    global lblPointsAccrued
    runningScore = runningScore + scoreThrow
    finalMessage = (f"{uname} your final score is: {runningScore}")
    lblFinalMessage["text"] = finalMessage
    lblPointsAccrued["text"] = runningScore
    frameCastResult.pack_forget()
    frameCastAgain.pack()

def writeFinalScoreToCSV():
    strName = uname
    intScore = runningScore
    print(f"{strName} , {intScore}")
    with open("C:\\Fishing_game\\Fisher.csv", mode="a", newline='') as csv_file:
    #setup heading names
        fieldnames = ['Name', 'Score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    # writer.writeheader()
        writer.writerow({'Name': strName, 'Score': intScore})
        csv_file.close()

def GetFish(DiceRoll):
 # count = 0
 data_arr = []
 # open file
 with open("C:\\Fishing_game\\Fishing.csv", 'r') as file:
 # set variable and reader
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data_arr.append(dict(row))
    global fishDisplay
    global fishPoints
    global scoreThrow
    global scoreKeep
    if DiceRoll == 1:
        flist = list(data_arr[0].values())
        fishDisplay = (flist[0])
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])
    elif DiceRoll == 2:
        flist = list(data_arr[1].values())
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])
        fishDisplay = (flist[0])
    elif DiceRoll == 3:
        flist = list(data_arr[2].values())
        fishPoints = (flist[3], flist[4])
        fishDisplay = (flist[0])
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])
    elif DiceRoll == 4:
        flist = list(data_arr[3].values())
        fishDisplay = (flist[0])
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])
    elif DiceRoll == 5:
        flist = list(data_arr[4].values())
        fishDisplay = (flist[0])
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])
    elif DiceRoll == 6:
        flist = list(data_arr[5].values())
        fishDisplay = (flist[0])
        scoreThrow = int(flist[4])
        scoreKeep = int(flist[3])  
# login Container
def login():
    global uname
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("Please fill in the fields!")
    else:
        if uname=="admin" and pwd=="admin":
            message.set("Login success")
            login_screen.destroy()
            fishGuiContainer()
        else:
            message.set("Wrong username or password!")
#Define loginform function
def Loginform():
    global login_screen
    global message
    global username
    global password
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x250")
    username = StringVar()
    password = StringVar()
    message = StringVar()
    Label(login_screen, width="300", text="please enter details below", bg="orange",fg="white").pack()
    Label(login_screen, text="Username * ").place(x=20,y=40)
    Entry(login_screen, textvariable=username).place(x=90,y=42)
    Label(login_screen, text="Password * ").place(x=20,y=80)
    Entry(login_screen, textvariable=password, show="*").place(x=90,y=82)
    Label(login_screen, text="", textvariable=message).place(x=95,y=100)
    Button(login_screen, text="Login", width=10, height=1, bg="orange",command=login).place(x=105, y=130)
    login_screen.mainloop()
    login_screen.destroy()
Loginform()