from re import sub
from tkinter import *


#creating a window
root =  Tk()

#decale the default variable
calc = ""

#definig the function
def addi():
    global calc
    calc += "+"
    pop['text'] = calc

def subi():
    global calc
    calc += "-"
    pop['text'] = calc

def divi():
    global calc
    calc += "/"
    pop['text'] = calc

def multipl():
    global calc
    calc += "*"
    pop['text'] = calc

def ze():
    global calc
    calc += "0"
    pop['text'] = calc

def on():
    global calc
    calc += "1"
    pop['text'] = calc

def tw():
    global calc
    calc += "2"
    pop['text'] = calc

def th():
    global calc
    calc += "3"
    pop['text'] = calc

def fo():
    global calc
    calc += "4"
    pop['text'] = calc

def fi():
    global calc
    calc += "5"
    pop['text'] = calc

def si():
    global calc
    calc += "6"
    pop['text'] = calc

def se():
    global calc
    calc += "7"
    pop['text'] = calc

def ei():
    global calc
    calc += "8"
    pop['text'] = calc

def ni():
    global calc
    calc += "9"
    pop['text'] = calc

def decii():
    global calc
    calc += "."
    pop["text"] = calc

def evali():
    global calc
    try:
        calc = eval(calc)
        pop["text"] = calc
        calc = ""
    except:
        pop['text'] = "AN ERROR OCCURRED"
        calc = ""

def cleari():
    global calc
    calc = ""
    pop["text"] = calc



#naming the window
root.title("A SIMPLE CALCULATOR")

#label and entry field
m = Label(root, text="CALCULATOR", font=(25))
pop = Label(root, text='', font=(50))

#operators box
adding = Button(root, text="+",height=2, width=5, command=addi)
subtracting = Button(root, text="-",height=2, width=5, command=subi)
dividing = Button(root, text="/",height=2, width=5, command=divi)
multiplying = Button(root, text="*",height=2, width=5, command=multipl)
equating = Button(root, text="=", height=10, width=13, command=evali)

#numbers
nine = Button(root, text="9", height=2, width=5, command=ni)
eight = Button(root, text="8", height=2, width=5, command=ei)
seven = Button(root, text="7", height=2, width=5, command=se)
six = Button(root, text="6", height=2, width=5, command=si)
five = Button(root, text="5", height=2, width=5, command=fi)
four = Button(root, text="4", height=2, width=5, command=fo)
three = Button(root, text="3", height=2, width=5, command=th)
two = Button(root, text="2", height=2, width=5, command=tw)
one = Button(root, text="1", height=2, width=5, command=on) 
zero = Button(root, text="0", height=2, width=5, command=ze)
ccc = Button(root, text="C", height=2, width=5, command=cleari)
deci = Button(root, text=".", height=2, width=5, command=decii)

#placing on screen
m.place(x=190, y=0)
pop.place(x=100, y=30)

#placiing operators
adding.place(x=100, y=60)
subtracting.place(x=150, y=60)
dividing.place(x=200, y=60)
multiplying.place(x=250, y=60)
equating.place(x=300, y=60)

#placing digits
nine.place(x=100, y=100)
eight.place(x=150, y=100)
seven.place(x=200, y=100)
six.place(x=250, y=100)
five.place(x=100, y=140)
four.place(x=150, y=140)
three.place(x=200, y=140)
two.place(x=250, y=140)
ccc.place(x=100, y=180)
one.place(x=150, y=180)
zero.place(x=200, y=180)
deci.place(x=250, y=180)

root.resizable(False, False)
root.geometry("500x500")



root.mainloop()
