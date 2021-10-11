from tkinter import *                  #import tkinter
from PIL import ImageTk,Image
from tkinter import PhotoImage
import tkinter as tk          # import PIL for image TK
from tkinter import *
from tkinter import messagebox


class MyFirstGUI:                       # Create a class to use GUI

    def __init__(self, master):         # create a function for 
        data = getData()
        
        self.master = master
        master.title("ATM")
        master.geometry("400x150")

        self.name = Label(master, text="Name:")
        self.name.grid(column=0, row=0)
        self.name2 = Label(master, text=data[2])
        self.name2.grid(column=1, row=0)

        # create Buttons for the widow 
        self.balance = Button(master, text="Balance", command=self.balance)
        self.balance.grid(row=1, column=0, padx=(10), pady=(50))

        self.withdrawl = Button(master, text="Withdrawl", command=self.withdrawl)
        self.withdrawl.grid(row=1, column=1, padx=(10), pady=(50))

        self.deposit = Button(master, text="Deposit", command=self.deposit)
        self.deposit.grid(row=1, column=2,padx=(10), pady=(50))
        self.close = Button(master, text="Close", command=master.quit)
        self.close.grid(row=1, column=3, padx=(10), pady=(50))


    def balance(self):     # create a function for  Balance that is attaached with self class
        data = getData()
        topb = Toplevel()
        topb.title("balance")  
        topb.geometry("240x300")

        self.imageb = tk.PhotoImage(file="downloadB.png");
        imageLabel = tk.Label(topb, image=self.imageb)
        imageLabel.grid(row=0, column=0,columnspan=2)

        self.name = Label(topb, text="Checking:")
        self.name.grid(row=1, column=0, pady=(20),sticky=W)
        self.name2 = Label(topb, text=data[3])
        self.name2.grid(row=1,column=1, pady=(20),sticky=W)


    def withdrawl(self):               # create a function for  withdrawl that is attaached with self class
        top = Toplevel()
        top.title("Withdrawl")
        top.geometry("275x340")

        self.imagew = tk.PhotoImage(file="downloadW.png");
        imageLabel = tk.Label(top, image=self.imagew)
        imageLabel.grid(row=0, column=0,columnspan=6)
        
        self.enter = Label(top, text="Enter amount") 
        self.enter.grid(column=0, row=1,pady=(20),sticky=W)

        self.input = Entry(top)
        self.input.grid(column=1, row=1)


        self.Withdrawl = Button(top, text="Withdrawl", command=self.subAmount)
        self.Withdrawl.grid(column=1,row=2,pady=(20))

    
    def deposit(self):      # create a function for  depsit that is attaached with self class
        data = getData()
        top3 = Toplevel()
        top3.title("deposit")
        top3.geometry("275x300")
        
        self.imaged = tk.PhotoImage(file="downloadd.png");
        imageLabel = tk.Label(top3, image=self.imaged)
        imageLabel.grid(row=0, column=0,columnspan=6)

        
        self.enter = Label(top3, text="Enter amount")
        self.enter.grid(column=0, row=1)   
        
        self.input = Entry(top3)
        self.input.grid(column=1, row=1)   
        
        self.Withdrawl = Button(top3, text="deposit", command=self.addAmount)
        self.Withdrawl.grid(column=1, row=2)


    def subAmount(self):     # create a function to call data form the file that is attaached with self class and subtraction amount 
        data = getData()
        checking = int(data[3])
        amount = int(self.input.get())

        while True:         # create a loop with condition for checking amount
            newChecking = checking - amount
            if newChecking < 0 or amount <0:
                msgError()
                break
            else:
                writeData(newChecking)
                msg()
                break

        
    def addAmount(self):      # create a function to call data form the file that is attaached with self class and add amout 
        data = getData()
        checking = int(data[3])
        amount = int(self.input.get())

        while True:
            if amount < 0:
                msgError()
                break
            else:
                newChecking = checking + amount
                writeData(newChecking)
                msg()
                break

def msg():                         # this function is dedicatied to give a successful massage if we put the a positive number or 0  
    data = getData()
    top2 = Toplevel()
    top2.title("success")
    
    enter = Label(top2, text="new balance")
    enter.grid(column=0, row=0)   
        
    enter = Label(top2, text=data[3])
    enter.grid(column=1, row=0)

def msgError():                   # this function dedicatied to give an error massage if we put the a nagative  number or 0 
    data = getData()
    top2 = Toplevel()
    top2.title("error")

    enter = Label(top2, text="amount must be positave")
    enter.grid(column=0, row=0)

    enter = Label(top2, text="balance")
    enter.grid(column=0, row=1)

    enter = Label(top2, text=data[3])
    enter.grid(column=1, row=1)

def getData():                                 # create a function to read data from the file 
    with open("user.txt", "r") as file:
        lines = file.readlines()
    
    lines = [s.strip() for s in lines]
    file.close()
    return lines

def writeData(checking):   # this function for reading and writing data
    with open("user.txt", "r") as file:
        lines = file.readlines()
    
    lines[3] = str(checking) + "\n"
    
    with open("user.txt", "w") as file:
        for line in lines:
            file.write(line)
            
        file.close()


def main():     # instantiation and pops up the window - infinite loop
    i=0
    while i < 3:

        username = input("Enter User: ")
        password = input("Enter Password: ")
        data = getData() 
        
        if username == str(data[0]) and password == str(data[1]):
            print("Welcome")
        
            root = Tk()
            my_gui = MyFirstGUI(root)
            root.mainloop()
            break
            
        else: 
            print("error username or password")
            i = i + 1
    print("Thanks")


# execute main() module
if __name__=="__main__":
    main()