import tkinter as tk

root = tk.Tk()
root.title("Mile to kilometer converson")
root.minsize(600,600)

change = False
text = tk.Label(text="Mile to Kilometer",font=("Arial",24,"bold"))
text.place(x=200,y=0)
def changemilekilo():
    global change
    if change:
        text["text"] = "Mile to Kilometer"
        change = False
    else:
        text["text"] = "Kilometer to Mile"
        change = True

def Quit():
    root.quit()

def Exchange():
    window = tk.Tk()
    window.title("Exchange")
    window.minsize(400,400)
    num = 0
    text = tk.Label(window, text="Conversor",font=("Arial", 24, "bold"))
    textResult = tk.Label(window,text=num,font=("Arial",24,"bold"))
    def Convert():
        textResult.place(x=50,y=150)
        if change:
            num = float(number.get()) * 1.6
            textResult["text"] = "Km: " + str(num)
        else:
            num = float(number.get()) / 1.6
            textResult["text"] = "Miles: " + str(num)
    def QuitWindow():
        window.destroy()
    buttonWQ = tk.Button(window, text="Quit", command=QuitWindow)
    buttonWC = tk.Button(window, text="Convert", command=Convert)
    text.place(x=50,y=0)
    buttonWQ.place(x=50,y=100)
    buttonWC.place(x=100,y=100)
    number = tk.Entry(window)
    number.place(x=50,y=50)



buttonC = tk.Button(text="Change order", command=changemilekilo)
buttonC.place(x=250,y=200)
buttonQ = tk.Button(text="Quit", command=Quit)
buttonQ.place(x=200,y=200)
buttonE = tk.Button(text="Exchange", command=Exchange)
buttonE.place(x=300,y=200)

root.mainloop()
