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



button1.grid(row = 0, column = 0)
button2.grid(row = 1, column = 0)
button3.grid(row = 2, column = 0)
button4.grid(row = 3, column = 0)
button5.grid(row = 4, column = 0)
button6.grid(row = 5, column = 0)
lol.grid(row = 5, column = 4)

image.grid(row = 4, column = 6, columnspan = 4, rowspan = 4)

button1.grid(row = 0, column = 0, ipadx = 55)
button2.grid(row = 1, column = 0 , ipadx = 71)
button3.grid(row = 2, column = 0 , ipadx = 74)
button4.grid(row = 3, column = 0 , ipadx = 88)
button5.grid(row = 4, column = 0 , ipadx = 69)
button6.grid(row = 5, column = 0 , ipadx = 50)


window.mainloop()
