from tkinter import *

window = Tk()
window.title("Jokes Generaitor")
window.geometry("700x700")

button1 = Button(window, text = "Black Humor")
button2 = Button(window, text = "Animals")
button3 = Button(window, text = "School")
button4 = Button(window, text = "All")
button5 = Button(window, text = "Standup")
button6 = Button(window, text = "VideoStandup")
image = Label(window, text = "Image")
lol = Label(window, text = "")
lol1 = Label(window, text = "")
lol2 = Label(window, text = "")
lol3 = Label(window, text = "<")
lol4 = Label(window, text = ">")


root = Tk()
root.title("Tk dropdown example")

# Add a grid
button11 = Frame(root)
button11.grid(column=0,row=0, sticky=(N,W,E,S) )
button11.columnconfigure(0, weight = 1)
button11.rowconfigure(0, weight = 1)
button11.pack(pady = 100, padx = 100)


# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Black Humor','Animals','School','All','Standups','Video Standups'}
tkvar.set('Black Humor') # set the default option

popupMenu = OptionMenu(button11, tkvar, *choices)
Label(button11, text="Categories").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)


button1.grid(row = 0, column = 0)
button2.grid(row = 1, column = 0)
button3.grid(row = 2, column = 0)
button4.grid(row = 3, column = 0)
button5.grid(row = 4, column = 0)
button6.grid(row = 5, column = 0)
lol.grid(row = 5, column = 2, ipadx = 15)
lol1.grid(row = 5, column = 3, ipadx = 15)
lol2.grid(row = 5, column = 4, ipadx = 15)
lol3.grid(row = 5, column = 5)
lol4.grid(row = 5, column = 7)



image.grid(row = 4, column = 6)

button1.grid(row = 0, column = 0, ipadx = 55)
button2.grid(row = 1, column = 0 , ipadx = 71)
button3.grid(row = 2, column = 0 , ipadx = 74)
button4.grid(row = 3, column = 0 , ipadx = 88)
button5.grid(row = 4, column = 0 , ipadx = 69)
button6.grid(row = 5, column = 0 , ipadx = 50)


window.mainloop()
