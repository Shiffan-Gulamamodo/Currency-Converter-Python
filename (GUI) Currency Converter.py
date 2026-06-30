#Shiffan Gulamamodo
#Imprting module from tkinter library
from tkinter import*
from tkinter import messagebox

#The function to convert Currency 
def Conversion():

    #Users Option to convert the currency from 
    fro = variable1.get()
    #Users Option to Convert currency to 
    to = variable2.get()
    
    # Validation for Input from the user
    try:
       Amount = float(Entry.get())  #Users Input
    except ValueError:
        messagebox.showerror("Error", "Please Input the amount to convert")
        return
    
    if float(Entry.get()) < 1:
             messagebox.showerror("Error", "Please enter a value greater than 0")
             return    
    
    #Main function to convert the currency 
    if ( fro == "GBP(Pounds)" and to == "EUR"):
          Total = round((Amount * 1.1398),2)
          ConvertedAmount = ('€', + Total)

    elif ( fro == "GBP(Pounds)" and to == "USD"):
            Total = round((Amount * 1.2157),2)
            ConvertedAmount = ('USD', + Total)

    elif ( fro == "GBP(Pounds)" and to == "CAD"):
            Total = round((Amount * 1.6279),2)
            ConvertedAmount = ('CAD', + Total)

    elif ( fro == "GBP(Pounds)" and to == "UAED"):
                Total = round((Amount * 4.4654),2)
                ConvertedAmount = ('د.إ', + Total)
                
    #Validation for empty option to convert the currency to 
    else:
        fro == "GBP(Pounds)" and to == "" 
        messagebox.showerror("Error", "Please select a Currency to Convert To")
        return

#Total Amount converted set as ConvertedAmount 
    Totaltext.set(ConvertedAmount)
    
#Resets the program function 
def Reset():
    variable2.set('')
    Entry.delete(0,END)
    Totaltext.set ('')

#End the program function
def Close():
    window.destroy()
    
#Create window
window = Tk()
window.geometry("620x240") #Adjust the size of the window
window.title ("Currency Convertor") #The title of the User interfae

# label text for title
label0= Label(window, text = "The Exchange Currency Convertor",
          foreground ="red", 
          font = ("Verdana", 14, "bold"))

#Dropdown menu options
Option1 = [
    "GBP(Pounds)"
]

Option2 = [
    "EUR",
    "USD",
    "CAD",
    "UAED",
]

# creating variables
variable1 = StringVar(window)
variable1.set("GBP(Pounds)")  #set the default option

#create dropdown optoin menu
option1 = OptionMenu(window, variable1, *Option1)
option1.config(width=10, font=("Verdana",12))

# creating variables 
variable2 = StringVar(window)
variable2.set(" ")  #set the default option as empty

#create dropdown optoin menu
option2 = OptionMenu(window, variable2, *Option2)
option2.config(width=10, font=("Verdana",12))

#Total converted amount Data type 
Totaltext = StringVar(window)

#create label for the small headers 
label1 = Label(window, text="Convert Currency From  : ",font = ("Verdana", 12, "bold"))
label2 = Label(window, text="Convert Currency To    : ",font = ("Verdana", 12, "bold"))
label3 = Label(window, text="Enter Amount in pounds : ",font = ("Verdana", 12, "bold"))
label4 = Label(window, text="Total Converted Amount : ",font = ("Verdana", 12, "bold"))
label5 = Label(window, text=" ",font = ("Verdana", 12),fg= "red", textvariable= Totaltext)

#Create a button
button1 = Button(window, text="Convert",command = Conversion, font = ("Verdana", 12, "bold"), height = 1, width = 10)
button2 = Button(window, text="Close", command = Close, font = ("Verdana", 12, "bold"), fg= "red")
button3 = Button (window, text = "Reset", command = Reset, font = ("Verdana", 12, "bold"), fg= "white", bg = "Green")

#Input Box
Entry = Entry(window, font= ("Verdana", 12), fg="green", width = 10)
        
#Adjusting space and position for dropdown list, label, button and input box
option1.grid(row = 2, column = 1, sticky = W, pady = 2)
option2.grid(row = 4, column = 1, sticky = W, pady = 2)

label0.grid (row=1, column=1, sticky = E, pady = 2)
label1.grid (row=2, column=0, sticky = E, pady = 2)
label2.grid (row=4, column=0, sticky = E, pady = 2)
label3.grid (row=5, column=0, sticky = E, pady = 2)
label4.grid (row=7, column=0, sticky = E, pady = 2)
label5.grid (row=7, column=1, sticky = W, pady = 2)

button1.grid (row=6, column=1, sticky = W, pady = 2)
button2.grid (row=8, column=1, sticky = E)
button3.grid (row=8, column=1, sticky = W)

Entry.grid(row=5, column=1, sticky = W, pady = 2)

#Execute tkinter
window.mainloop()
 
