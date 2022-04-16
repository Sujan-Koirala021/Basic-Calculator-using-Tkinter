# Basic Calculator with addition, subtraction, multiplication and division using tkinter
# Sujan Koirala, Institute of Engineering, Pulchowk

from ast import Lambda
from tkinter import *
mode = "none"
root =Tk()
root.title("Simple Calculator")
# Creating input field
myEntry = Entry(root, width = 35, borderwidth=5)
myEntry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def clickButton(num):
    current = myEntry.get()
    myEntry.delete(0, END)    
    myEntry.insert(0,  str(current) + str(num))

def clearButton():
    myEntry.delete(0, END)
    
def addButton():
    global mode
    mode = "addition"
    first_num = myEntry.get()
    global f_num
    f_num = float(first_num)
    myEntry.delete(0, END)

def subtractButton():
    global mode
    mode = "subtraction"
    first_num = myEntry.get()
    global f_num
    f_num = float(first_num)
    myEntry.delete(0, END)

def multiplyButton():
    global mode 
    mode = "multiplication"
    first_num = myEntry.get()
    global f_num
    f_num = float(first_num)
    myEntry.delete(0, END)

def divideButton():
    global mode
    mode = "division"
    first_num = myEntry.get()
    global f_num
    f_num = float(first_num)
    myEntry.delete(0, END)
    
def equalButton():
    second_num = myEntry.get()
    myEntry.delete(0, END)    
    
    # Checking for the mode of operation
    if mode == "addition":
        myEntry.insert(0, str(f_num + float(second_num)))
    if mode == "subtraction":
        myEntry.insert(0, str(f_num - float(second_num)))
    if mode == "multiplication":
        myEntry.insert(0, str(f_num * float(second_num)))         
    if mode == "division":
        myEntry.insert(0, str(f_num / float(second_num)))

# Define buttons
button1 = Button(root, text = "1" , padx = 40, pady =20, command = lambda: clickButton(1))
button2 = Button(root, text = "2" , padx = 40, pady =20, command = lambda: clickButton(2))
button3 = Button(root, text = "3" , padx = 40, pady =20, command = lambda: clickButton(3))
button4 = Button(root, text = "4" , padx = 40, pady =20, command = lambda: clickButton(4))
button5 = Button(root, text = "5" , padx = 40, pady =20, command = lambda: clickButton(5))
button6 = Button(root, text = "6" , padx = 40, pady =20, command = lambda: clickButton(6))
button7 = Button(root, text = "7" , padx = 40, pady =20, command = lambda: clickButton(7))
button8 = Button(root, text = "8" , padx = 40, pady =20, command = lambda: clickButton(8))
button9 = Button(root, text = "9" , padx = 40, pady =20, command = lambda: clickButton(9))
button0 = Button(root, text = "0" , padx = 40, pady =20, command = lambda: clickButton(0))

buttonAdd = Button(root, text = "+" , padx = 39, pady =20, command = addButton)
buttonSubtract = Button(root, text = "-" , padx = 41, pady =20, command = subtractButton)
buttonMultiply = Button(root, text = "*" , padx = 40, pady =20, command = multiplyButton)
buttonDivide = Button(root, text = "/" , padx = 41, pady =20, command = divideButton)

buttonEqual = Button(root, text = "=" , padx = 91, pady =20, command = equalButton)
buttonClear = Button(root, text = "Clear" , padx = 79, pady =20, command = clearButton)


# Putting buttons on the screen
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)

button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)

button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)

button0.grid(row = 4, column = 0)
buttonClear.grid(row = 4, column = 1, columnspan = 2)
buttonAdd.grid(row = 5, column = 0)
buttonEqual.grid(row = 5, column = 1, columnspan = 2)

buttonSubtract.grid(row = 6, column = 0)
buttonMultiply.grid(row = 6, column = 1)
buttonDivide.grid(row = 6, column = 2)

root.mainloop()