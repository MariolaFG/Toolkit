from tkinter import *
root = Tk()

label1 = Label(root, text = "Enter your expression")
label1.grid(row = 0)

labelHelp = Label(root,text = " ")
labelHelp.grid(row = 0, column = 1)

label2 = Label(root, text = "Your result is:")
label2.grid(row=2, column=0)

def evaluate(event):
    data = e.get()
    ans.configure(text = "Answer." + str(eval(data)))
    
e = Entry(root)

e.bind("<Return>", evaluate)
e.grid(row=1)

ans = Label(root)
ans.grid(row=2,column=1)

root.mainloop()


