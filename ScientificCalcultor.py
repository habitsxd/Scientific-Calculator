#**********************  ScientificCalculator.py  *********************
#
# Name: Maxxfield Smith
#
# Course: CSCI 1470
#
# Assignment: Term Project
#**********************************************************

from tkinter import*
from tkinter import messagebox
import math

# creates the tkinter window and the calculator frame, and grid for the buttons------------------------------------------------------------
root = Tk()
root.configure(bg = 'gray20')
root.title('Scientific Calculator')
root.resizable(width = False, height = False)
root.geometry('463x547')

calc = Frame(root) #creates a frame inside the window for the calculator
calc.grid()
calc.configure(bg = 'gray20')
#---------------------------------------------------------------------------------------------------------------------------------------------
class Calc():
    def __init__(self):
        '''initalizes the calculator class with the following variables and flags'''
        self.total = 0
        self.current = ''
        self.inputval = True
        self.checksum = False
        self.operator = ''
        self.result = False

    def num(self, num):
        '''used to call numbers into the textbox'''
        self.result = False
        firstnum = textbox.get()
        secnum = str(num)
        if self.inputval:
            self.current = secnum
            self.inputval = False
        else:
            if secnum == '.':
                if secnum in firstnum:
                    return
            self.current = firstnum + secnum
        self.display(self.current)

    def sumtotal(self):
        '''used for the equal button'''
        self.result = True
        self.current = float(self.current)
        if self.checksum == True:
            self.mathstuff()
        else:
            self.total = float(textbox.get())

    def display(self, value):
        '''handles deleting and inserting values into the textbox'''
        textbox.delete(0, END)
        textbox.insert(0, value)

    def mathstuff(self):
        '''handles arithmetic operations'''
        if self.op == 'add':
            self.total += self.current
        if self.op == 'sub':
            self.total -= self.current
        if self.op == 'multi':
            self.total *= self.current
        if self.op == 'divide':
            self.total /= self.current
        if self.op == 'mod':
            self.total %= self.current
        self.inputval = True
        self.checksum = False
        self.total = float(self.total)
        if self.total % 1 == 0:
            self.total = int(self.total)
        else:
            self.total = float(self.total)
        self.display(self.total)
        return

    def operation(self, op):
        '''calls arithmetic operations and sets up flags for the equal sign'''
        self.op = op
        self.current = float(self.current)
        if self.checksum:
            self.mathstuff()
        elif not self.result:
            self.total = self.current
            self.inputval = True
        self.checksum = True
        self.result = False

    def CE(self):
        '''clears current entry from the textbox, and self.current'''
        self.result = False
        self.current = ''
        self.display(0)
        self.inputval = True

    def C(self):
        '''clears current and total from the display'''
        self.CE()
        self.total = 0


    def posneg(self):
        '''displays the negative value of the current value in display'''
        self.result = False
        self.current = -(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def pi(self):
        '''displays the value of pi'''
        self.result = False
        self.current = math.pi
        self.display(float(self.current))

    def e(self):
        '''displays the value of e'''
        self.result = False
        self.current = math.e
        self.display(float(self.current))

    def root(self):
        '''displays the square root of the current number in display'''
        self.result = False
        self.current = math.sqrt(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def xsqr(self):
        '''squares the current value in the display'''
        self.result = False
        self.current = math.pow(float(textbox.get()), 2)
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def xcbe(self):
        '''cubes the current value in the display'''
        self.result = False
        self.current = math.pow(float(textbox.get()), 3)
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def factorial(self):
        '''displays the factorial of current value'''
        self.result = False
        self.current = math.factorial(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def log(self):
        '''displays the logarithm of the current value'''
        self.result = False
        self.current = math.log10(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def ln(self):
        '''displays the natural logarithm of the current value'''
        self.result = False
        self.current = math.log(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def log2(self):
        '''displays the log base 2 of the current value'''
        self.result = False
        self.current = math.log2(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def sin(self):
        '''displays the sine of the current value'''
        self.result = False
        self.current = math.sin(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def cos(self):
        '''displays the cosine of the current value'''
        self.result = False
        self.current = math.cos(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def tan(self):
        '''displays the tangent of the current value'''
        self.result = False
        self.current = math.tan(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def asin(self):
        '''displays the inverse sine of the current value'''
        self.result = False
        self.current = math.asin(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def acos(self):
        '''displays the inverse cosine of the current value'''
        self.result = False
        self.current = math.acos(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

    def atan(self):
        '''displays the inverse tangent of the current value'''
        self.result = False
        self.current = math.atan(float(textbox.get()))
        if self.current % 1 == 0:
            self.current = int(self.current)
        else:
            self.current = float(self.current)
        self.display(self.current)

addval = Calc()

#creates the textbox -----------------------------------------------------------------------------------------------------------------
textbox = Entry(calc, font = ('expressway', 20, 'bold'),bg = 'light gray', bd = 20, width = 28, justify = 'right')
textbox.grid(row = 0, column = 0, columnspan = 4, pady = 1)
textbox.insert(0, 0)

# creates the number pad.-------------------------------------------------------------------------
numpad = '987654321'
i = 0
btn = []
for row in range(2, 5):
    for column in range(3):
        btn.append(Button(calc, width = 6, height = 2,  font = ('expressway', 20, 'bold'), bd = 4, justify = RIGHT, ##
        text = numpad[i], bg = 'black', fg = 'light gray'))
        btn[i].grid(row = row, column = column, pady = 1)
        btn[i]['command'] = lambda x = numpad [i]: addval.num(x)
        i += 1

zero_btn = Button(calc, width = 6, height = 2,  font = ('expressway', 20, 'bold'), bd = 4, justify = RIGHT,
text = '0',command = lambda: addval.num(0), bg = 'black', fg = 'light gray').grid(row = 5, column = 0, pady = 1) ##

# creates the standard mode buttons for basic arithmetic-----------------------------------------------------------------------------------

clear_btn = Button(calc, text = 'CE', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = addval.CE).grid(row = 1, column = 0, pady = 1) ##clears the current value, total stays the same

clear_all = Button(calc, text = 'C', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = addval.C).grid(row = 1, column = 1, pady = 1) ## clears current, total and everything in calc memory

add_btn = Button(calc, text = '+', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.operation('add')).grid(row = 1, column = 3, pady = 1) ## adds two values together

sub_btn = Button(calc, text = '-', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.operation('sub')).grid(row = 2, column = 3, pady = 1) ## subtracts two values

sqrt_btn = Button(calc, text = '.', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.root()).grid(row = 1, column = 2, pady = 1) ## squares current value

mul_btn = Button(calc, text = '*', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.operation('multi')).grid(row = 3, column = 3, pady = 1) ## multiplies two values

div_btn = Button(calc, text = chr(247), width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.operation('divide')).grid(row = 4, column = 3, pady = 1) ## divides two values

deci_btn = Button(calc, text = '.', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.num('.')).grid(row = 5, column = 1, pady = 1) ## enters a decimal point into text box

posneg_btn = Button(calc, text = chr(177), width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = addval.posneg).grid(row = 5, column = 2, pady = 1) ## returns the negative value of current number

equal_btn = Button(calc, text = '=', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4, ## performs called operations and gives result of operations
                        bg = 'light gray', command = addval.sumtotal).grid(row = 5, column = 3, pady = 1)

mod_btn = Button(calc, text = '%', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.operation('mod')).grid(row = 3, column = 6, pady = 1) ## returns the remainder of two numbers


# creates the buttons for scientific mode--------------------------------------------------------------------------------------------------

#----------------- TRIG FUNCTIONS & SPECIAL MATH SYMBOLS------------------------------------------------------------------------------
pi_btn = Button(calc, text = 'π', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.pi()).grid(row = 5, column = 4, pady = 1) ##

sin_btn = Button(calc, text = 'sin', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.sin()).grid(row = 1, column = 4, pady = 1) ##

cos_btn = Button(calc, text = 'cos', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.cos()).grid(row = 1, column = 5, pady = 1) ##

tan_btn = Button(calc, text = 'tan', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.tan()).grid(row = 1, column = 6, pady = 1) ##

arcsin_btn = Button(calc, text = 'arcsin', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.asin()).grid(row = 2, column = 4, pady = 1) ##

arccos_btn = Button(calc, text = 'arccos', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.acos()).grid(row = 2, column = 5, pady = 1) ##

arctan_btn = Button(calc, text = 'arctan', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.atan()).grid(row = 2, column = 6, pady = 1) ##

factorial_btn = Button(calc, text = '!', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.factorial()).grid(row = 5, column = 5, pady = 1) ## factorial button

e_btn = pi2_btn = Button(calc, text = 'e', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.e()).grid(row = 5, column = 6, pady = 1) ## shows the numeric value of e


#-----------------------------EXPONENTS-------------------------------------------------------------------------

xsqr_btn = Button(calc, text = 'x\u00b2', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.xsqr()).grid(row = 3, column = 4, pady = 1) ## button to square current value

xcbe_btn = Button(calc, text = 'x\u00b3', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.xcbe()).grid(row = 3, column = 5, pady = 1) ## button to cube current value

#------------------------LOGARITHMS------------------------------------------------------------------------------

log_btn = Button(calc, text = 'log', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.log()).grid(row = 4, column = 4, pady = 1) ##button for logarithm base 10

log2_btn = Button(calc, text = 'log\u2082', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.log2()).grid(row = 4, column = 5, pady = 1) ## logarithm base 2

ln_btn = Button(calc, text = 'ln', width = 6, height = 2, font = ('expressway', 20, 'bold'), bd = 4,
                        bg = 'light gray', command = lambda: addval.ln()).grid(row = 4, column = 6, pady = 1) ## natural logarathim base e

lbl = Label(calc, text = 'Scientific Calculator', font = ('expressway', 27, 'bold'), justify = CENTER, bg = 'gray20', fg = 'light gray')
lbl.grid(row = 0, column = 4, columnspan = 3) #creates a lable for scientific mode
#-------------------------------------------------------------------------------------------------------------------------------

# create drop down menus -------------------------------------------------------------------------------------------------------

def quit():
    '''quits the program when called'''
    quit = messagebox.askyesno('Scientific Calculator','Are you sure you would like to exit?')
    if quit == True:
        root.destroy()
        return

def secret():
    '''hehe'''
    secret = messagebox.askyesno('Scientific Calculator',"Are you sure you want to do this?")
    if secret == True:
        secret = messagebox.askokcancel('Scientific Calculator',"You really don't want to do this.")
        if secret == True:
            secret = messagebox.askokcancel('Scientific Calculator', 'This is your last chance, buddy.')
            if secret == True:
                textbox.insert(0,'58008')
    return

def scientific(): # switches frame size from standard to scientific
    root.resizable(width = False, height = False)
    root.geometry('820x547')

def standard(): # switches frame size from scientific to standard
    root.resizable(width = False, height = False)
    root.geometry('463x547')

menubar = Menu(calc) # creates a menubar in the calculator frame

filemenu = Menu(menubar, tearoff = 0) # created a dropdown menu to switch from standard to scientific
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'Standard', command = standard)
filemenu.add_command(label = 'Scientific', command = scientific)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = quit)

dgrmenu = Menu(menubar, tearoff = 0) # creates a menu to switch from degree and radian mode for trig functions
menubar.add_cascade(label = "Mode", menu = dgrmenu)
dgrmenu.add_command(label = 'Degrees')
dgrmenu.add_command(label = 'Radians')

hiddenmenu = Menu(menubar, tearoff = 0) # love you Daniel
menubar.add_cascade(label = "Don't Click", menu = hiddenmenu)
hiddenmenu.add_command(label = "Really Don't Click", command = secret)


root.config(menu = menubar)
root.mainloop()


# a few bugs and features I would like to add in the future. would like to add error messages for zero division and other similar things. self.total is not
#clearing as I would like it to when trying to perform multiple operations before pressing the equal button. will add a functioning degree and radian mode
#in the future, but it's a little out of my scope right now.
